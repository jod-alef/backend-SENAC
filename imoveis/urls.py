from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('imoveis/', views.list_imoveis, name='list-imoveis'),
    path('imoveis/editar/<int:imovel_id>', views.editar_imovel, name='editar_imovel'),
    path('imoveis/excluir/<int:imovel_id>', views.excluir_imovel, name='excluir_imovel'),
    path('inquilinos/', views.list_inquilinos, name='list-inquilinos'),
]
