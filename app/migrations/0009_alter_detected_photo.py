# Generated by Django 4.2.8 on 2023-12-29 11:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0008_alter_detected_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="detected",
            name="photo",
            field=models.ImageField(upload_to="detected/"),
        ),
    ]
