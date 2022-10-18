from msilib.schema import AdminExecuteSequence
from pickletools import unicodestring1
from django.db import models


class unit(models.Model):
    id = models.IntegerField(db_column='UNIT', primary_key=True, unique=True)
    name = models.CharField(db_column='NAME', max_length=3)

    class Meta:
        managed = False
        db_table = 'UNIT'

    def __str__(self):
        return self.name

class depart(models.Model):
    id = models.IntegerField(db_column='DEPART', primary_key=True, unique=True)
    numlist = models.IntegerField(db_column='LIST')
    date = models.DateField(db_column='DATA1')
    time = models.TimeField(db_column='TIME1')
    type = models.IntegerField(db_column='EMPTY')
    id_unit1 = models.OneToOneField(unit, db_column='UNIT1', related_name ='UNIT1', to_field='id', on_delete = models.DO_NOTHING)    #Возможно не нужен будет всегда сорт
    id_unit2 = models.OneToOneField(unit, db_column='UNIT2', related_name ='UNIT2', to_field='id', on_delete = models.DO_NOTHING)    #Возможно не нужен будет всегда к-к

    class Meta:
        managed = False
        db_table = 'DEPART'

    def __str__(self):
        return self.numlist

class sort(models.Model):
    id = models.IntegerField(db_column='SORT', primary_key=True, unique=True)
    sort = models.CharField(db_column='TIP', max_length=3)

    class Meta:
        managed = False
        db_table = 'SORT'

    def __str__(self):
        return self.sort

class coming(models.Model):
    id = models.IntegerField(db_column='TRAIN1', primary_key=True, unique=True)
    sort = models.OneToOneField(sort, db_column='SORT', to_field='id', on_delete = models.DO_NOTHING)  #nvarchar(2)

    class Meta:
        managed = False
        db_table = 'TRAIN1'

    def __str__(self):
        return self.sort       

class cargo(models.Model):
    id = models.IntegerField(db_column='CARGO', primary_key=True, unique=True)
    cargo = models.CharField(db_column='NAME', max_length=25)

    class Meta:
        managed = False
        db_table = 'CARGO'

    def __str__(self):
        return self.cargo

class station(models.Model):
    id = models.IntegerField(db_column='STATION', primary_key=True, unique=True)
    station = models.CharField(db_column='NAZV', max_length=50)

    class Meta:
        managed = False
        db_table = 'STATION'

    def __str__(self):
        return self.station

class client(models.Model):
    id = models.IntegerField(db_column='ADDRESS1', primary_key=True, unique=True)
    name = models.CharField(db_column='NAME', max_length=50)

    class Meta:
        managed = False
        db_table = 'ADDRESS1'

    def __str__(self):
        return self.name

class wagons(models.Model):
    id = models.IntegerField(db_column='TRAIN2', primary_key=True, unique=True)
    order = models.IntegerField(db_column='PORYDOK')
    number = models.CharField(db_column='NOMER', max_length=8)
    weight = models.FloatField(db_column='WEIGHT2')
    id_coming = models.OneToOneField(coming, db_column='TRAIN1', to_field='id', on_delete = models.DO_NOTHING)
    id_depart = models.OneToOneField(depart, db_column='DEPART', to_field='id', on_delete = models.DO_NOTHING)
    id_cargo = models.OneToOneField(cargo, db_column='CARGO2', to_field='id', on_delete = models.DO_NOTHING)
    id_station = models.OneToOneField(station, db_column='STATION2', to_field='id', on_delete = models.DO_NOTHING)
    id_client = models.OneToOneField(client, db_column='ADDRESS2', to_field='id', on_delete = models.DO_NOTHING)   #Возможно не нужен будет

    class Meta:
        managed = False
        db_table = 'TRAIN2'

    def __str__(self):
        return self.number

class mailing_list(models.Model):
    #id_client = models.OneToOneField(client, db_column='ADDRESS2', to_field='id', on_delete = models.DO_NOTHING)
    id_client =  models.IntegerField(db_column='id_client', null=True)
    name = models.CharField(db_column='name', max_length=50, null=True)
    email = models.EmailField(db_column='email', ) #unique=True
    send = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)

    class Meta:
        db_table = 'mailing_list'

    def __str__(self):
        return str(self.name) + " " + str(self.email) + " " + str(self.send)

class mailing_list_admin(models.Model):
    name = models.CharField(db_column='fio', max_length=50)
    email = models.EmailField(db_column='email', ) #unique=True
    send = models.BooleanField(default=True)

    class Meta:
        db_table = 'mailing_list_admin'