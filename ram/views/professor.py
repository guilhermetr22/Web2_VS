from django.contrib.auth import login, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.views.generic import CreateView

User = get_user_model()

from ram.forms import ProfessorCadastroForm


class ProfessorCadastroView(CreateView):
    model = User
    form_class = ProfessorCadastroForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professor'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return HttpResponseRedirect('/')











