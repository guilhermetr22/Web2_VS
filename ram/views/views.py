from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView, CreateView

#from ram.forms import UserForm, ProfessorForm, CoordenadorForm
from django.contrib.auth import authenticate, login

from ram.forms import ProfessorCadastroForm, UserForm, ProfessorForm
from ram.models import User


def login(request):
    USERNAME = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect("home.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('home.html')

class SignUpView(TemplateView):
    template_name = 'registration/signup.html'

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        professor_form = ProfessorForm(request.POST, instance=request.user.professor)

        if user_form.is_valid() and professor_form.is_valid():
            user_form.save()
            professor_form.save()
            return render(request,'/', {})
        else:
            print('It is not working')
    else:
        user_form = UserForm(instance=request.user )
        professor_form = ProfessorForm(instance=request.user.professor)

    return render(request, 'registration/professor_form.html', {'user_form':user_form, 'professor_form': professor_form})




def professor_profile(request):
    return render(request, 'professor/professor_profile.html',{})


def home(request):
    return render(request, 'home.html')




