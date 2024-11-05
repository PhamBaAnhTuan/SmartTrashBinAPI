import cv2
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image, ImageDraw, ImageFont
import requests 
import time

last_request_time = 0
request_interval = 5

# Tải mô hình đã lưu
model = load_model('model.h5')

# Mở camera
cap = cv2.VideoCapture(0)

# Kích thước và vị trí của vùng focus
focus_width, focus_height = 320, 320
focus_x, focus_y = (640 - focus_width) // 2, (480 - focus_height) // 2  # Đặt vị trí ở giữa

# URL của API để cập nhật phân loại rác
api_url = "http://127.0.0.1:8000/api/trashtype/1"

# Bộ trừ nền
bg_subtractor = cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=25, detectShadows=True)

while True:
    # Đọc khung hình từ camera
    ret, frame = cap.read()
    if not ret:
        print("Không thể mở camera.")
        break
    
    # Chuyển đổi khung hình từ BGR sang RGB
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Cắt khung hình trong vùng focus
    focus_region = image_rgb[focus_y:focus_y + focus_height, focus_x:focus_x + focus_width]

    # Áp dụng bộ trừ nền lên vùng focus để phát hiện vật thể
    fg_mask = bg_subtractor.apply(focus_region)

    # Đếm số lượng pixel khác không trong fg_mask để xác định có vật thể mới
    non_zero_count = np.count_nonzero(fg_mask)
    threshold = 1000  # Ngưỡng để xác định có vật thể mới, có thể điều chỉnh

    # Biến để lưu thông điệp
    message = ""
    if non_zero_count < threshold:
        message = "Vui lòng đưa rác vào ô."
    else:
        # Tiền xử lý khung hình
        image_resized = cv2.resize(focus_region, (224, 224))
        image_array = img_to_array(image_resized)
        image_array = np.expand_dims(image_array, axis=0)
        image_array /= 255.0

        # Dự đoán
        predictions = model.predict(image_array)
        predicted_class = np.argmax(predictions, axis=1)
        confidence = np.max(predictions)

        # Ngưỡng độ tin cậy
        confidence_threshold = 0.7
        if confidence >= confidence_threshold:
            # Lấy nhãn lớp
            class_labels = ['organic', 'inOrganic']
            predicted_label = class_labels[predicted_class[0]]
            message = predicted_label

            current_time = time.time()
            if current_time - last_request_time > request_interval:
                # Cập nhật lên server
                payload = {"name": predicted_label}
                response = requests.put(api_url, json=payload)
                if response.status_code == 200:
                    print(f"Cập nhật thành công: {predicted_label}")
                else:
                    print(f"Cập nhật thất bại: {response.text}")

                last_request_time = current_time
        else:
            message = "Không thể xác định loại rác."

    # Vẽ vùng focus lên khung hình
    cv2.rectangle(frame, (focus_x, focus_y), (focus_x + focus_width, focus_y + focus_height), (0, 255, 255), 2)

    # Hiển thị thông điệp lên khung hình bằng Pillow
    pil_img = Image.fromarray(frame)
    draw = ImageDraw.Draw(pil_img)
    try:
        font = ImageFont.truetype("arial.ttf", 32)
    except IOError:
        font = ImageFont.load_default()

    draw.text((10, 30), message, font=font, fill=(0, 255, 0))

    # Chuyển đổi lại sang NumPy array
    frame = np.array(pil_img)

    # Hiển thị khung hình
    cv2.imshow('Camera', frame)

    # Nhấn 'q' để thoát
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Giải phóng camera và đóng tất cả cửa sổ
cap.release()
cv2.destroyAllWindows()
