from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .models import MyUser, MyUserManager, User1, User2
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm, SignupForm, LogoutForm
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import get_user_model
import cv2
from django.http import StreamingHttpResponse
from django.views.decorators import gzip
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from wsgiref.util import FileWrapper
from django.contrib.auth.models import Group
from django.shortcuts import render
from django.contrib.auth import get_user_model
from .forms import *
from .models import *

User = get_user_model()

@login_required
def home(request):
    return render(request, 'home.html')

def create_users(request):
    user1 = User.objects.create_user('user1', 'user1@example.com', 'password1')
    user2 = User.objects.create_user('user2', 'user2@example.com', 'password2')

    group1 = User1.objects.create(name='Group 1')
    group2 = User2.objects.create(name='Group 2')

    group1.user_set.add(user1)
    group2.user_set.add(user2)

    return render(request, 'create_users.html')


@login_required
def my_view(request):
    if request.user.groups.filter(name='User1').exists():
        return render(request, 'user1_call.html')
    elif request.user.groups.filter(name='User2').exists():
        return render(request, 'user2_call.html')
    else:
        return render(request, 'default_template.html')

@login_required
def account(request):
    user = request.user
    context = {
        'username': user.username,
        'email': user.email,
        # Другие переменные с информацией о пользователе
    }
    return render(request, 'personalaccount.html', context=context)



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                error_message = 'Неправильное имя пользователя или пароль'
                form = LoginForm()
                return render(request, 'login.html', {'form': form, 'error_message': error_message})

    else:
        form = AuthenticationForm(request)
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    if request.method == 'GET':
        form = LogoutForm(request.POST)
        if form.is_valid():
            logout(request)
            return redirect('home')
    else:
        form = LogoutForm()
    return redirect('home')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']
            MyUser.objects.create_user(username=username, email=email, password=password)
            #form.save()

            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('home')
        else:
            messages.error(request, 'Пожалуйста, исправьте ошибки в форме')
    else:
        form = SignupForm()
    return render(request, 'login.html', {'form': form})

def home(request):
    if request.user.is_authenticated:

        # Если пользователь авторизован, отображаем кнопку личного кабинета
        return render(request, 'home.html', {'user': request.user})
    else:

        # Если пользователь не авторизован, отображаем кнопки входа и регистрации
        return render(request, 'home.html')

def video_chat(request):
    task = 'Здесь будет задание'
    return render(request, 'user2_call.html', {'task': task})


def chat_view(request, username):
    sender = request.user
    receiver = get_object_or_404(User, username=username)
    messages = Message.objects.filter(sender__in=[sender, receiver], receiver__in=[sender, receiver]).order_by('timestamp')
    context = {'messages': messages, 'receiver': receiver}
    return render(request, 'chat.html', context)

def download_file(request, file_id):
    file = get_object_or_404(File, id=file_id)
    response = FileResponse(file.file, as_attachment=True, filename=file.filename)
    return response

def my_video_view(request):
    return render(request, 'user2_call.html')

# Create your views here.

