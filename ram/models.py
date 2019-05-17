from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.conf import settings
from django.db.models.signals import post_save


class User(AbstractUser):
    is_coordenador = models.BooleanField(default=False)
    is_professor = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    email = models.EmailField(('E-mail'),max_length=50, unique=True, default='', null=True)
    #password = models.CharField(('SENHA'), max_length=100, default="", null=False)
    username = models.CharField(('Nome de Usuário'), max_length=20, null=False, unique=True)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = ('user')
        verbose_name_plural = ('users')

    def get_name(self):
        '''
        Returns the full name
        '''
        full_name = '%s' % (self.name)
        return full_name.strip()

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Materia(models.Model):
    INITIAL_ID = 1
    COMP = 1
    MEC = 2

    cursos = [
        (COMP, 'Engenharia de computação'),
        (MEC, 'Engenharia Mecânica')
    ]




class Professor (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    materias = models.CharField(max_length=20, default="", null=False)

    def __str__(self):
        return self.user.name()


class Coordenador(models.Model):
    user = models.OneToOneField(Professor, on_delete=models.CASCADE, primary_key=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default='0')
    curso = models.CharField(max_length=20, default="", null=False)


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self,name, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """

        if not email:
            raise ValueError('É necessário um email')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
