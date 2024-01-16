from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Produto

def cadastrar_produto(req):
    if req.method == "GET":
        return render(req, 'cadastrar_produto.html')
    elif req.method == "POST":
        produto = Produto(
            nome = req.POST.get('nome'),
            preco = req.POST.get('preco'),
            validade = req.POST.get('validade'),
            quantidade = req.POST.get('quantidade'),
        )
        produto.save()
        return redirect('/estoque/cadastrar_produto')

def listar_produtos(req):
    produtos = Produto.objects.all()
    preco = req.GET.get('preco')
    if preco:
        produtos = produtos.filter(preco__gt=preco)
    return render(req, 'listar_produtos.html', {'produtos': produtos})

def deletar_produto(req, id):
    Produto.objects.get(id=id).delete()
    return redirect('/estoque/listar_produtos')