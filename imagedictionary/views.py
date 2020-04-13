from django.contrib.auth.models import User, Group
from rest_framework import viewsets

from .serializers import UserSerializer, HistorySerializer
from .models import History


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


# Create your views here.
class HistoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows History to be viewed or edited
    """
    queryset = History.objects.all()
    serializer_class = HistorySerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    