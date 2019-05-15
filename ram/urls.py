from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from ram.views import views, coordenador, professor
from ram.views.professor import ProfessorCadastroView as professor_view

urlpatterns = [
    url(r'^$', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    #url(r'^admin/', admin.site.urls),
    url(r'^logout/', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^accounts/signup/', views.SignUpView.as_view(), name='signup'),
    url(r'^accounts/signup/professor', professor.ProfessorCadastroView.as_view(), name='cadastro_professor'),
    url(r'^accounts/signup/coordenador', coordenador.CoordenadorCadastroView.as_view(), name='cadastro_coordenador'),
#   url(r'^about_me/$', views.user_profile),

]


