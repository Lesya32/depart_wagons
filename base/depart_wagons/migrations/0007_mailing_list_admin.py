# Generated by Django 4.0.8 on 2022-10-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('depart_wagons', '0006_rename_fio_mailing_list_admin_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailing_list',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
