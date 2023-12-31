# Generated by Django 3.0.7 on 2021-08-03 19:52

import ckeditor.fields
from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210803_1151'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='milage',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='miles',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='car',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='car',
            name='features',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('PakAssist', 'PakAssist'), ('Power Steering', 'Power Steering'), ('Reersing Camera', 'Reersing Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset')], max_length=193),
        ),
    ]
