# Generated by Django 4.2.6 on 2024-01-30 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shoes', '0012_remove_shoes_quantity_size_size_delete_quantity'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size39',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size40',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size41',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size42',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size43',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size44',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size45',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Size46',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='shoes',
            name='size',
        ),
        migrations.DeleteModel(
            name='Size',
        ),
        migrations.AddField(
            model_name='shoes',
            name='size39',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size39'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='size40',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size40'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='size41',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size41'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='size42',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size42'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='size43',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size43'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='size44',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size44'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='size45',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size45'),
        ),
        migrations.AddField(
            model_name='shoes',
            name='size46',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='shoes.size46'),
        ),
    ]
