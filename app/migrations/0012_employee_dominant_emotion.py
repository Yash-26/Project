# Generated by Django 4.2.8 on 2024-03-01 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_employee_heart_rate'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='dominant_emotion',
            field=models.CharField(default=2, max_length=200),
            preserve_default=False,
        ),
    ]
