# Generated by Django 4.2.16 on 2024-11-21 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_detectedemotion_alter_detected_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detectedemotion',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
