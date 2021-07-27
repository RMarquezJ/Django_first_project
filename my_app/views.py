from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse

def root (request):
  return redirect('/blogs')

def index(request):
  return HttpResponse('placeholder para luego mostrar una lista de todos los blogs')

def new(request):
  return HttpResponse('Placeholder para mostrar nuevo formulario para crear nuevo blog')

def create(request):
  return redirect('/')

def show(request,num):
  return HttpResponse(f'Placeholder para mostrar el blog numero: {num}')

def edit(request,num):
  return HttpResponse(f'Placeholder para editar el blog {num}')

def destroy(request,num):
  return redirect ('/blogs')

def json(request):
  return JsonResponse({
    'first_name': 'Rodrigo',
    'last_name':'Marquez',
    'age':31
  })

def other_func(request):
  return HttpResponse('A todos')