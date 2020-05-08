from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import UserRegisterSerializer, UserDetailSerializer, HistorySerializer
from .models import History
from .permissions import IsUser


class UserCreateView(generics.CreateAPIView):
    """
    API endpoint for creating new users
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer


class UserDetailView(generics.RetrieveAPIView):
    """
    API endpoint that allows users to view their profile.
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    permission_classes = [IsAuthenticated, IsUser]


# Create your views here.
class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows History to be viewed or edited
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    