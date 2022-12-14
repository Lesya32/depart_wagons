# Generated by Django 4.0.8 on 2022-10-13 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cargo',
            fields=[
                ('id', models.IntegerField(db_column='CARGO', primary_key=True, serialize=False, unique=True)),
                ('cargo', models.CharField(db_column='NAME', max_length=25)),
            ],
            options={
                'db_table': 'CARGO',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='client',
            fields=[
                ('id', models.IntegerField(db_column='ADDRESS1', primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(db_column='NAME', max_length=50)),
            ],
            options={
                'db_table': 'ADDRESS1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='coming',
            fields=[
                ('id', models.IntegerField(db_column='TRAIN1', primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'db_table': 'TRAIN1',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='depart',
            fields=[
                ('id', models.IntegerField(db_column='DEPART', primary_key=True, serialize=False, unique=True)),
                ('numlist', models.IntegerField(db_column='LIST')),
                ('date', models.DateField(db_column='DATA1')),
                ('time', models.TimeField(db_column='TIME1')),
                ('type', models.IntegerField(db_column='EMPTY')),
            ],
            options={
                'db_table': 'DEPART',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='sort',
            fields=[
                ('id', models.IntegerField(db_column='SORT', primary_key=True, serialize=False, unique=True)),
                ('sort', models.CharField(db_column='TIP', max_length=3)),
            ],
            options={
                'db_table': 'SORT',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='station',
            fields=[
                ('id', models.IntegerField(db_column='STATION', primary_key=True, serialize=False, unique=True)),
                ('station', models.CharField(db_column='NAZV', max_length=50)),
            ],
            options={
                'db_table': 'STATION',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='wagons',
            fields=[
                ('id', models.IntegerField(db_column='TRAIN2', primary_key=True, serialize=False, unique=True)),
                ('order', models.IntegerField(db_column='PORYDOK')),
                ('number', models.CharField(db_column='NOMER', max_length=8)),
                ('weight', models.FloatField(db_column='WEIGHT2')),
            ],
            options={
                'db_table': 'TRAIN2',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='mailing_list_admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(db_column='fio', max_length=50)),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('send', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'mailing_list_admin',
            },
        ),
        migrations.CreateModel(
            name='mailing_list',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(db_column='email', max_length=254, unique=True)),
                ('send', models.BooleanField(default=True)),
                ('id_client', models.OneToOneField(db_column='ADDRESS2', on_delete=django.db.models.deletion.DO_NOTHING, to='depart_wagons.client')),
            ],
            options={
                'db_table': 'mailing_list',
            },
        ),
    ]
