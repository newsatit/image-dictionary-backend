from django.contrib.auth.models import User, Group
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

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


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })


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

    