from django.shortcuts import render, HttpResponse

def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome, idade))

def soma(request, n1, n2):
    return HttpResponse('<h1>A soma de {} e {} é igual a: {}</h1>'.format(n1, n2, n1+n2))

def subtracao(request, n1, n2):
    return HttpResponse('<h1>A subtração de {} e {} é igual a: {}</h1>'.format(n1, n2, n1-n2))

def divisao(request, n1, n2):
    return HttpResponse('<h1>A divisão de {} e {} é igual a: {}</h1>'.format(n1, n2, n1/n2))

def multiplicacao(request, n1, n2):
    return HttpResponse('<h1>A multiplicação de {} e {} é igual a: {}</h1>'.format(n1, n2, n1*n2))
