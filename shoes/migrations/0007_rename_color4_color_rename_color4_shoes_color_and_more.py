# Generated by Django 4.2.6 on 2024-01-13 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0006_color2_color3_color4_color5_rename_color_color1_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Color4',
            new_name='Color',
        ),
        migrations.RenameField(
            model_name='shoes',
            old_name='color4',
            new_name='color',
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='color1',
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='color2',
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='color3',
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='color5',
        ),
        migrations.DeleteModel(
            name='Color1',
        ),
        migrations.DeleteModel(
            name='Color2',
        ),
        migrations.DeleteModel(
            name='Color3',
        ),
        migrations.DeleteModel(
            name='Color5',
        ),
    ]
