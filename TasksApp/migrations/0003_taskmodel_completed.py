# Generated by Django 5.0 on 2024-06-10 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TasksApp', '0002_taskmodel_img_alter_taskmodel_create_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='completed',
            field=models.BooleanField(default=False),
        ),
    ]