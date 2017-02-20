from rest_framework.views import APIView
from rest_framework.response import Response
from core.models import Party, Project, Transaction
from .serializers import PartySerializer, ProjectSerializer, TransactionSerializer


class PartyListAPI(APIView):
    def get(self, request):
        parties = Party.objects.all()
        serializer = PartySerializer(parties, many=True)
        return Response(serializer.data)


class ProjectListAPI(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class TransactionListAPI(APIView):
    def get(self, request):
        transactions = Transaction.objects.all()
        serializer = TransactionSerializer(transactions, many=True)
        return Response(serializer.data)
