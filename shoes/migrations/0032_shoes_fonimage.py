# Generated by Django 4.2.6 on 2024-02-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0031_color1_color2_color3_shoes_color1_shoes_color2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='fonImage',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
