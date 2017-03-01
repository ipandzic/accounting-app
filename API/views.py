from rest_framework import generics
from core.models import Party, Project, Transaction
from .serializers import PartySerializer, ProjectSerializer, TransactionSerializer


class PartyListAPI(generics.ListCreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class PartyDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer


class ProjectListAPI(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TransactionListAPI(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class TransactionDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
