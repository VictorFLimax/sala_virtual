from rest_framework import viewsets

from core import models , serializers



class AnexoViewSet(viewsets.ModelViewSet):
    queryset = models.Anexo.objects.all()
    serializer_class = serializers.AnexoSerializer

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = models.Participante.objects.all()
    serializer_class = serializers.ParticipantesSerializer

class SalaAulaViewSet(viewsets.ModelViewSet):
    queryset = models.SalaAula.objects.all()
    serializer_class = serializers.SalaAulaSerializer

class SalaAulaAnexoViewSet(viewsets.ModelViewSet):
    queryset = models.SalaAula.objects.all()
    serializer_class = serializers.SalaAulaAnexoSerializer

class ParticipanteSalaAnexoViewSet(viewsets.ModelViewSet):
    queryset = models.ParticipanteSalaAnexo.objects.all()
    serializer_class = serializers.ParticipanteSalaAnexoSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentarioSerializer

class ComentarioAnexoViewSet(viewsets.ModelViewSet):
    queryset = models.Comentario.objects.all()
    serializer_class = serializers.ComentarioAnexoSerializer

