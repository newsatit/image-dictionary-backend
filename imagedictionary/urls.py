from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token 
from rest_framework.urlpatterns import format_suffix_patterns

from imagedictionary import views

user_create = views.UserCreateView.as_view()
user_detail = views.UserDetailView.as_view()
history_list = views.HistoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('users/', user_create),
    path('users/<int:pk>/', user_detail),
    path('histories/', history_list)
]