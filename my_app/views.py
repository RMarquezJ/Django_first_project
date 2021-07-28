from django.http.response import JsonResponse
from django.shortcuts import redirect, render, HttpResponse
from time import gmtime, localtime, strftime

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

def images(request):
  context = {
    'images': ['https://jumbo.vteximg.com.br/arquivos/ids/423699/Cerveza-58%C2%B0-lata-473-cc.jpg?v=637517622726630000', 'https://www.elcielo.cl/tienda/1449-medium_default/cerveza-cristal-lata-470cc-46.jpg', 'https://jumbo.vteximg.com.br/arquivos/ids/262978/Cerveza-Becker-Lata-350-cc-2-2956.jpg?v=636749442883230000', 'https://www.ccu.cl/wp-content/uploads/2018/03/escudo-1-e1564002214549.png'
  ]}
  return render(request,'pics.html', context)

def local(request):
  context = {
    "time": strftime('%d-%m-%Y %H:%M hrs.', localtime())
  }
  return render(request, 'time.html', context)

def other_func(request):
  return HttpResponse('A todos')