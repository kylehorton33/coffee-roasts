# Generated by Django 3.2.8 on 2021-10-13 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0002_roast_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='bean',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
