# Generated by Django 4.2.6 on 2024-01-31 11:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0020_rename_size_shoes_size41_shoes_size42_shoes_size43_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoes',
            name='size39',
            field=models.CharField(default=django.utils.timezone.now, max_length=55),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shoes',
            name='size40',
            field=models.CharField(default=django.utils.timezone.now, max_length=55),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size41',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size42',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size43',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size44',
            field=models.CharField(max_length=55),
        ),
        migrations.AlterField(
            model_name='shoes',
            name='size45',
            field=models.CharField(max_length=55),
        ),
        migrations.DeleteModel(
            name='Size41',
        ),
        migrations.DeleteModel(
            name='Size42',
        ),
        migrations.DeleteModel(
            name='Size43',
        ),
        migrations.DeleteModel(
            name='Size44',
        ),
        migrations.DeleteModel(
            name='Size45',
        ),
    ]
