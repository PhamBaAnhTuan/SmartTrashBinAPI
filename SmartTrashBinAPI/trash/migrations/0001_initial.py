# Generated by Django 5.1.1 on 2024-10-04 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organic', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
                ('inOrganic', models.DecimalField(blank=True, decimal_places=1, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrashType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
    ]
