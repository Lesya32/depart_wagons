# Generated by Django 4.0.8 on 2022-10-13 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('depart_wagons', '0005_mailing_list_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mailing_list_admin',
            old_name='fio',
            new_name='name',
        ),
    ]