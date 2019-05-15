from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.urls import include
from django.contrib.auth import views as auth_views
from ram.views import views, professor, coordenador

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'', include('ram.urls')),
    #url(r'^accounts/', include('django.contrib.auth.urls')),
    path('', auth_views.LoginView.as_view(), {'template_name': 'registration/login.html'}, name='login'),
    #url(r'^admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/signup/professor', professor.ProfessorCadastroView.as_view(), name='cadastro_professor'),
    path('accounts/signup/coordenador', coordenador.CoordenadorCadastroView.as_view(), name='cadastro_coordenador'),

]
