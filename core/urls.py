
from django.contrib import admin
from django.urls import path, include
from .views import home, editarUser, updateUser, deleteUser, visuaUser, salvarUser, cadUsuarios, salvarCliente, cadCliente, visuaCliente, deleteCliente, updateCliente, editarCliente, cadProduto, salvarProduto, visuaProduto, editarProduto, updateProduto, deleteProduto


urlpatterns = [

    
    path('', home, name="inicio"),


    #Funções de usuário

    path('cadastrar_usuario', cadUsuarios, name="cadastrar_usuario"),
    path('salvar_usuario', salvarUser, name="salvar_usuario"),
    path('visualizar_usuario', visuaUser, name="visualizar_usuario"),
    path('editar_usuario/<int:id>', editarUser, name="editar_usuario"),
    path('update_usuario/<int:id>', updateUser, name="update_usuario"),
    path('delete_usuario/<int:id>', deleteUser, name="delete_usuario"),



    #Funções de clientes
    path('cadastrar_cliente', cadCliente, name="cadastrar_cliente"),
    path('salvar_cliente', salvarCliente, name="salvar_cliente"),
    path('visualizar_cliente', visuaCliente, name="visualizar_cliente"),
    path('editar_cliente/<int:id>', editarCliente, name="editar_cliente"),
    path('update_cliente/<int:id>', updateCliente, name="update_cliente"),
    path('delete_cliente/<int:id>', deleteCliente, name="delete_cliente"),


    #Funções de produtos
    path('cadastrar_produto', cadProduto, name="cadastrar_produto"),
    path('salvar_produto', salvarProduto, name="salvar_produto"),
    path('visualizar_produto', visuaProduto, name="visualizar_produto"),
    path('editar_produto/<int:id>', editarProduto, name="editar_produto"),
    path('update_produto/<int:id>', updateProduto, name="update_produto"),
    path('delete_produto/<int:id>', deleteProduto, name="delete_produto"),

 
]

