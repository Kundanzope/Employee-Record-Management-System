# Generated by Django 3.1.3 on 2022-05-10 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0006_auto_20220504_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeentry',
            name='photo',
            field=models.ImageField(default='empicon.png', upload_to='media'),
        ),
    ]
