# Generated by Django 4.0.3 on 2022-03-15 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JulaneHotel', '0005_reservation_custid'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='status',
            field=models.CharField(default='SOME STRING', max_length=20),
        ),
    ]
