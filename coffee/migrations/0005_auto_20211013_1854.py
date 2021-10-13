# Generated by Django 3.2.8 on 2021-10-13 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffee', '0004_auto_20211013_1835'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bean',
            old_name='origin_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='bean',
            old_name='delivery_date',
            new_name='delivered_on',
        ),
        migrations.RenameField(
            model_name='roast',
            old_name='roast_profile',
            new_name='degree_of_roast',
        ),
        migrations.RenameField(
            model_name='roast',
            old_name='quantity',
            new_name='green_quantity',
        ),
        migrations.RemoveField(
            model_name='bean',
            name='origin_region',
        ),
        migrations.RemoveField(
            model_name='bean',
            name='origin_variety',
        ),
        migrations.AddField(
            model_name='bean',
            name='region',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='bean',
            name='variety',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AddField(
            model_name='roast',
            name='roast_quantity',
            field=models.DecimalField(decimal_places=1, default=342, help_text='Yeild weight in grams', max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='bean',
            name='altitude_max',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='bean',
            name='altitude_min',
            field=models.PositiveIntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='bean',
            name='certified_fairtrade',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bean',
            name='certified_organic',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bean',
            name='certified_rainforestalliance',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bean',
            name='decaffeinated',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bean',
            name='drying',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bean',
            name='harvest',
            field=models.CharField(blank=True, max_length=140),
        ),
        migrations.AlterField(
            model_name='bean',
            name='process',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
