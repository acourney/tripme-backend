# Generated by Django 4.0.4 on 2022-04-15 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_alter_trip_destination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trip',
            name='destination',
            field=models.CharField(max_length=500),
        ),
    ]
