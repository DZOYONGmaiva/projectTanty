from django.contrib import messages
from django.contrib.auth import get_user_model, login, authenticate, logout
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from Utilisateur.models import Utilisateur
# Create your views here.
from django.contrib.auth.decorators import login_required


User = get_user_model()
@login_required(login_url='login')
def compte(request):
    return render(request, 'Utilisateur/compte.html')

def contact(request):
    return render(request, 'Utilisateur/contact.html')

def aPropos(request):
    return render(request, 'Utilisateur/apropos.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        print(user)
        users = Utilisateur.objects.all()
        for elt in users:
            if elt.username == username:
                print(elt.username)
                print('b')
                if elt.password == password:
                    print(elt.password)
                    print('c')
                    login(request, user)
                    print('succès')
                    return redirect('compte')
        if user:
            print(5)
            login(request, user)
            print(6)
            return redirect('compte')
        else:
            print(7)
            messages.error(request, "Erreur de connexion, veillez entrer les informations correctes")
            print(8)
            return redirect('login')
        print(9)
    return render(request, 'Utilisateur/login.html')

def signup(request):
    if request.method == "POST":
        first_name = request.POST.get("nom")
        last_name = request.POST.get("prenom")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        email=email,
                                        password=password)
        login(request, user)
        return redirect('compte')
    return render(request, 'Utilisateur/login.html')

def Logout(request):
    logout(request)
    return redirect('index')

def carriere(request):
    return render(request, 'Utilisateur/carriere.html')

@login_required(login_url='login')
def modifCompte(request):
    user = request.User
    dic = {'first_name': user.first_name,
           'last_name': user.last_name,
           'username': user.username,
           'email': user.email,
           'password': user.password}
    return render(request, 'Utilisateur/modifCompte.html')

def Contacter(request):
    utilisateur = request.user
    print(utilisateur)
    if request.method == 'POST':
        print('hello')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message
        }

        message = '''
            {}

            From: {}
            '''.format(data['message'], data['email'])
        send_mail(data['subject'], message, '', ['ntfoodstanty2022@gmail.com'])
    return render(request,'Utilisateur/contact.html')