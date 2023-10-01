from django.shortcuts import render, redirect
from .models import Usuarios, Cliente, Produto



def home(request):
    return render(request, "index.html")

def cadUsuarios(request):
    usuarios = Usuarios.objects.all()
    return render(request, "addUser.html", {"usuarios": usuarios})

def salvarUser(request):
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get("nome")
    novo_usuario.sobrenome = request.POST.get("sobrenome")
    novo_usuario.email = request.POST.get("email")
    novo_usuario.permissao = request.POST.get("permissao")
    novo_usuario.save()
    usuarios = Usuarios.objects.all()
    return render(request, "visuaUser.html", {"usuarios": usuarios})

def editarUser(request, id):
    usuario = Usuarios.objects.get(id=id)
    return render(request, "updateUser.html", {"usuario": usuario})

def updateUser(request, id):
    vnome = request.POST.get("nome")
    usuario = Usuarios.objects.get(id=id)
    usuario.nome = vnome
    usuario.save()
    return redirect(visuaUser)

def deleteUser(request, id):
    usuario = Usuarios.objects.get(id=id)
    usuario.delete()
    return redirect(visuaUser)

def visuaUser(request):
    usuarios = Usuarios.objects.all()
    return render(request, "visuaUser.html", {"usuarios": usuarios})




#Funções de Clientes
def cadCliente(request):
    clientes = Cliente.objects.all()
    return render(request, "addCliente.html", {"clientes": clientes})

def salvarCliente(request):
    novo_cliente = Cliente()
    novo_cliente.nome = request.POST.get("nome")
    novo_cliente.email = request.POST.get("email")
    novo_cliente.telefone = request.POST.get("telefone")
    novo_cliente.save()


    clientes = Cliente.objects.all()
    return render(request, "visuaCliente.html", {"clientes": clientes})

def editarCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    return render(request, "updateCliente.html", {"cliente": cliente})

def updateCliente(request, id):
    vnome = request.POST.get("nome")
    cliente = Cliente.objects.get(id=id)
    cliente.nome = vnome
    cliente.save()
    return redirect(visuaCliente)

def deleteCliente(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect(visuaCliente)

def visuaCliente(request):
    clientes = Cliente.objects.all()
    return render(request, "visuaCliente.html", {"clientes": clientes})




#Funções de Produtos
def cadProduto(request):
    produtos = Produto.objects.all()
    return render(request, "addProduto.html", {"produtos": produtos})

def salvarProduto(request):
    novo_produto = Produto()
    novo_produto.nome = request.POST.get("nome")
    novo_produto.email = request.POST.get("email")
    novo_produto.telefone = request.POST.get("telefone")
    novo_produto.save()

    produtos = Produto.objects.all()
    return render(request, "visuaProduto.html", {"produtos": produtos})

def editarProduto(request, id):
    produto = Produto.objects.get(id=id)
    return render(request, "updateProduto.html", {"produto": produto})

def updateProduto(request, id):
    vnome = request.POST.get("nome")
    produto = Produto.objects.get(id=id)
    produto.nome = vnome
    produto.save()
    return redirect(visuaProduto)

def deleteProduto(request, id):
    produto = Produto.objects.get(id=id)
    produto.delete()
    return redirect(visuaProduto)

def visuaProduto(request):
    produtos = Produto.objects.all()
    return render(request, "visuaProduto.html", {"produtos": produtos})

