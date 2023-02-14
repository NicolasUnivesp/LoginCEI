from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from app.forms import LivrosForm
from app.models import Livros


def home(request):
    return render(request, 'home.html')


# Formulário de cadastro de usuários
def create(request):
    return render(request, 'create.html')


# Inserção dos dados dos usuários no banco
def store(request):
    data = {}
    if request.POST['password'] != request.POST['password-conf']:
        data['msg'] = 'Senha e confirmação de senha diferentes!'
        data['class'] = 'alert-danger'
    else:
        user = User.objects.create_user(request.POST['user'], request.POST['email'], request.POST['password'])
        user.first_name = request.POST['name']
        user.save()
        user.user_permissions.add(28)
        data['msg'] = 'Usuário cadastrado com sucesso!'
        data['class'] = 'alert-success'
    return render(request, 'create.html', data)


# Formulário do painel de login
def painel(request):
    return render(request, 'painel.html')


# Processa o login
def dologin(request):
    data = {}
    user = authenticate(username=request.POST['user'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')
    else:
        data['msg'] = 'Usuário ou Senha inválidos!'
        data['class'] = 'alert-danger'
        return render(request, 'painel.html', data)


# Página inicial do dashboard
def dashboard(request):
    return render(request, 'dashboard/home.html')


def logouts(request):
    logout(request)
    return redirect('/painel/')


def changePassword(request):
    user = User.objects.get(email=request.user.email)
    user.set_password('123456')
    user.save()
    logout(request)
    return redirect('/painel/')


def index(request):
    data = {}
    all = Livros.objects.all()
    paginator = Paginator(all, 2)
    pages = request.GET.get('page')
    data['db'] = paginator.get_page(pages)
    search = request.GET.get('search')
    if search:
        data['db'] = Livros.objects.filter(titulo__icontains=search)
    else:
        data['db'] = Livros.objects.all()
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = LivrosForm()
    return render(request, 'form.html', data)


def createLivro(request):
    form = LivrosForm(request.POST or None)
    if form.is_valid():
        data = {}
        form.save()
        return redirect('/index/')


def view(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    return render(request, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    data['form'] = LivrosForm(instance=data['db'])
    return render(request, 'form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Livros.objects.get(pk=pk)
    form = LivrosForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/index/')


def delete(request, pk):
    db = Livros.objects.get(pk=pk)
    db.delete()
    return redirect('/index/')
