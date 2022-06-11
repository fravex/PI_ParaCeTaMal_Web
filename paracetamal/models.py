# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import User

class AnvisaNome(models.Model):
    id = models.IntegerField(primary_key=True)
    nomeproduto = models.CharField(db_column='nomeProduto', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anvisa_nome'

    def __str__(self) -> str:
        return self.nomeproduto

class AnvisaNomePrincipioativo(models.Model):
    idproduto = models.OneToOneField(AnvisaNome, models.DO_NOTHING, db_column='idProduto', primary_key=True)  # Field name made lowercase.
    idprincipio = models.ForeignKey('AnvisaPrincipioativo', models.DO_NOTHING, db_column='idPrincipio')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anvisa_nome_principioativo'
        unique_together = (('idproduto', 'idprincipio'),)


class AnvisaPrincipioativo(models.Model):
    id_pativo = models.IntegerField(db_column='id_pAtivo', primary_key=True)  # Field name made lowercase.
    nome_pativo = models.CharField(db_column='nome_pAtivo', max_length=250, blank=True, null=True)  # Field name made lowercase.
    translated_pativo = models.CharField(db_column='translated_pAtivo', max_length=250, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anvisa_principioativo'



class BigtableNomes(models.Model):
    id_principal = models.IntegerField(blank=True, primary_key=True)
    nome = models.CharField(max_length=250, blank=True, null=True)
    tipo_origem = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'bigtable_nomes'


class DrugbankAnvisa(models.Model):
    drugbank = models.OneToOneField('DrugbankNome', models.DO_NOTHING, primary_key=True)
    id_pativo = models.ForeignKey(AnvisaPrincipioativo, models.DO_NOTHING, db_column='id_pAtivo')  # Field name made lowercase.
    matchingvalue = models.FloatField(db_column='matchingValue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'drugbank_anvisa'
        unique_together = (('drugbank', 'id_pativo'),)


class DrugbankInteracao(models.Model):
    drugbank_id1 = models.OneToOneField('DrugbankNome', related_name= 'drugbank_id1', db_column='drugbank_id1', primary_key=True, on_delete=models.CASCADE)
    drugbank_id2 = models.ForeignKey('DrugbankNome', related_name= 'drugbank_id2', db_column='drugbank_id2', on_delete=models.CASCADE)

    class Meta:
        managed = False
        db_table = 'drugbank_interacao'
        unique_together = (('drugbank_id1', 'drugbank_id2'),)


class DrugbankNome(models.Model):
    drugbank_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'drugbank_nome'


class Usuario(User):
    pass