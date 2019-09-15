from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.UserProfileEditView, name='user-profile'),
]
