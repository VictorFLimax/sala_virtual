from django.db import models

# Create your models here.

class ModelBase(models.Model):
    id = models.AutoField(primary_key=True)
    modified_at = models.DateTimeField(auto_now=True, null = False)
    created_at = models.DateTimeField(auto_now_add=True, null = False)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        managed = True

class Anexo(ModelBase):
    nome = models.CharField(max_length=40)
    tipo = models.CharField(max_length=20)
    caminho_anexo = models.CharField(max_length = 50)
    servidor = models.CharField(max_length=100)

    class Meta:
        db_table = 'anexo'


class Participante(ModelBase):
    email = models.CharField(max_length=40)
    nome = models.CharField(max_length=100)
    apelido = models.CharField(max_length = 20)
    senha = models.CharField(max_length=20)
    perfil = models.CharField(max_length=1)
    class Meta:
        db_table = 'participante'

class SalaAula(ModelBase):
    instituicao = models.CharField(max_length=100)
    data_aula = models.DateField(auto_now=False, auto_now_add=True)
    disciplina = models.CharField(max_length=40)
    conteudo = models.TextField()
    class Meta:
        db_table = 'sala_aula'



class SalaAulaAnexo(ModelBase):
    id_anexo = models.ForeignKey(
        to  = 'Anexo',
        on_delete = models.DO_NOTHING,
        db_column = 'id_anexo',
        null = False,
        blank = False
    )
    id_sala_aula = models.ForeignKey(
        to = 'SalaAula',
        on_delete = models.DO_NOTHING,
        db_column = 'id_sala_aula',
        null = False,
        blank = False
    )
    class Meta:
        db_table = 'sala_aula_anexo'

class ParticipanteSalaAnexo(ModelBase):
    id_sala_aula = models.ForeignKey(
        to = 'SalaAula',
        on_delete = models.DO_NOTHING,
        db_column = 'id_sala_aula',
        null = False,
        blank = False
    )
    id_participante = models.ForeignKey(
        to = 'Participante',
        on_delete = models.DO_NOTHING,
        db_column = 'id_participante',
        null = False,
        blank = False
    )
    class Meta:
        db_table = 'participante_sala_anexo'


class Comentario(ModelBase):
    data_aula = models.DateField(auto_now=False, auto_now_add=True)
    texto = models.TextField()
    tipo = models.CharField(max_length=1)
    id_sala_aula = models.ForeignKey(
        to = 'SalaAula',
        on_delete = models.DO_NOTHING,
        db_column = 'id_sala_aula',
        null = False,
        blank = False
    )
    id_participante = models.ForeignKey(
        to = 'Participante',
        on_delete = models.DO_NOTHING,
        db_column = 'id_participante',
        null = False,
        blank = False
    )

    class Meta:
        db_table = 'comentario'

class ComentarioAnexo(ModelBase):
    id_anexo = models.ForeignKey(
        to = 'Anexo',
        on_delete = models.DO_NOTHING,
        db_column = 'id_anexo',
        null = False,
        blank = False
    )
    id_comentario = models.ForeignKey(
        to = 'Comentario',
        on_delete = models.DO_NOTHING,
        db_column = 'id_comentario',
        null = False,
        blank = False

    )
    class Meta:
        db_table = 'comentario_anexo'

