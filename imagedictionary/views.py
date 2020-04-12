from django.shortcuts import render
from rest_framework import viewsets
from .serializers import HistorySerializer
from .models import History

# Create your views here.
class HistoryView(viewsets.ModelViewSet):
    """
    API endpoint that allows History to be viewed or edited
    """
    serializer_class = HistorySerializer
    queryset = History.objects.all()