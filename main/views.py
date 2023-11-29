from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Создаем нового пользователя
        user = User.objects.create_user(username=username, password=password, email=email)

        # Автоматически выполняем вход после регистрации
        login(request, user)

        # Перенаправляем пользователя на другую страницу после регистрации
        return redirect('home')

    # Если запрос GET, отображаем шаблон с формой регистрации
    return render(request, 'main/register.html')

def index(request):
    data = {
        'title':'Главная страница',
        'values': ['1 ', '12 ', '123 ']
    }
    return render(request, 'main/index.html', data)

def about(request):
     return render(request, 'main/about.html')

def contacts(request):
     return render(request, 'main/contacts.html')
