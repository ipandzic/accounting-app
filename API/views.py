from rest_framework import generics
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
from core.models import Party, Project, Transaction
from .permissions import IsOwnerOrReadOnly
from .serializers import PartySerializer, ProjectSerializer, TransactionSerializer


class PartyCreateAPIView(generics.CreateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PartyDetailAPIView(generics.RetrieveAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class PartyUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class PartyDeleteAPIView(generics.DestroyAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class PartyListAPIView(generics.ListAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProjectCreateAPIView(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProjectUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class ProjectDeleteAPIView(generics.DestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class TransactionCreateAPIView(generics.CreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class TransactionDetailAPIView(generics.RetrieveAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class TransactionUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class TransactionDeleteAPIView(generics.DestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class TransactionListAPIView(generics.ListAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
