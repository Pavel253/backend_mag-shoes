# Generated by Django 4.2.6 on 2024-02-03 22:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0026_alter_shoes_quantity_delete_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoes',
            name='color',
        ),
    ]
