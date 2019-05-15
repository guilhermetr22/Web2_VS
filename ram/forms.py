from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from ram.models import Professor, Coordenador, User

User = get_user_model()

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email')

class ProfessorForm(forms.ModelForm):
   class Meta:
       model = Professor
       fields = ('materias',)


class CoordenadorForm(forms.ModelForm):
    class Meta:
        model = Coordenador
        fields = ('curso', )


class ProfessorCadastroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email',)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_professor = True
        if commit:
            user.save()
        return user


class CoordenadorCadastroForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_coordenador = True
        if commit:
            user.save()
        return user

