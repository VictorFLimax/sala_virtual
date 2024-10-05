from rest_framework import serializers

from core import models


class AnexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Anexo
        fields = '__all__'

class ParticipantesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Participante
        fields = '__all__'


class SalaAulaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SalaAula
        fields = '__all__'

class SalaAulaAnexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SalaAulaAnexo
        fields = '__all__'

class ParticipanteSalaAnexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ParticipanteSalaAnexo
        fields = '__all__'

class ComentarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Comentario
        fields = '__all__'

class ComentarioAnexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ComentarioAnexo
        fields = '__all__'

