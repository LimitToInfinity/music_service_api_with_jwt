from django.urls import path # , include
from .views import ListSongsView, ListCreateSongsView, SongsDetailView, LoginView, RegisterUsersView
# from . import views
# from rest_framework import routers

# router = routers.DefaultRouter()
# router.register('music', views.)

urlpatterns = [
    path('songs/', ListSongsView.as_view(), name="songs-all"),
    path('songs/create', ListCreateSongsView.as_view(), name="songs-list-create"),
    path('songs/<int:pk>/', SongsDetailView.as_view(), name="songs-detail"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/register/', RegisterUsersView.as_view(), name="auth-register"),
    # path("", include(router.urls))
]
