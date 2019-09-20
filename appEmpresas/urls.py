from django.urls import path
from .views import empresa_detail_view, empresa_create_view, empresa_lista_view, empresa_delete_view


urlpatterns = [
    path('info/<str:slug>/', empresa_detail_view, name='empresa-lista'),
    path('admin/<str:slug>/', empresa_detail_view, name='empresa-admin'),
    path('lista/', empresa_lista_view, name='empresa-lista'),
    path('create/', empresa_create_view, name='empresa-create'),
    path('delete/<str:slug>/', empresa_delete_view, name='empresa-delete'),
    #path('<str:slug>/edit/', blog_post_update_view),
]
