# Create your models here.
import re
from urllib.parse import urlparse

from django import forms
from django.conf import settings
from django.contrib.auth.models import (AbstractBaseUser, BaseUserManager,
                                        PermissionsMixin)
from django.core import validators
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_staff, is_superuser, img, cpf, curso, data_nasc, **extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError(_('O nome fornecido deve ser definido'))

        if not img:
            raise ValueError('A image fornecida deve ser definido')

        if not cpf:
            raise ValueError('A image fornecida deve ser definido')

        if not curso:
            raise ValueError('A image fornecida deve ser definido')

        if not data_nasc:
            raise ValueError('A image fornecida deve ser definido')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email,
                          is_staff=is_staff, is_active=True, img=img, cpf=cpf, curso=curso, data_nasc=data_nasc,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, img, cpf, curso, data_nasc, email=None, password=None, **extra_fields):
        return self._create_user(username, email, img, cpf, curso, data_nasc, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        user = self._create_user(username, email, password, True, True,
                                 **extra_fields)
        user.is_active = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):

    CURSOS_CHOICES = (
        ("Administração", "Administração"),
        ("Biblioteca Setorial", "Biblioteca Setorial"),
        ("Ciências Biológicas", "Ciências Biológicas"),
        ("Enfermagem", "Enfermagem"),
        ("História", "História"),
        ("Letras", "Letras"),
        ("Matemática", "Matemática"),
        ("Medicina", "Medicina"),
        ("Nutrição", "Nutrição"),
        ("Núcleo de Assistência Estudantil (NAE)",
         "Núcleo de Assistência Estudantil (NAE)"),
        ("Pedagogia", "Pedagogia"),
        ("Restaurante Universitário (RU)", "Restaurante Universitário (RU)"),
        ("Sistemas de Informação", "Sistemas de Informação"),
        ("Outro", "Outro"),
    )

    username = models.CharField(_('username'), max_length=15, unique=True,
                                help_text=_('Required. 15 characters or fewer. Letters, \
                    numbers and @/./+/-/_ characters'),
                                validators=[
        validators.RegexValidator(
            re.compile('^[\w.@+-]+$'),
            _('Enter a valid username.'),
            _('invalid'))])
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. \
                    Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(_('trusty'), default=False,
                                    help_text=_('Designates whether this user has confirmed his account.'))
    # News
    img = models.ImageField(null=True, blank=True,
                            upload_to='imagens/', verbose_name='*Foto')
    cpf = models.CharField(max_length=14, null=True,
                           verbose_name=('*CPF'),  unique=True)
    curso = models.CharField(max_length=38,  null=True, choices=CURSOS_CHOICES,
                             verbose_name=('*Curso'))

    data_nasc = models.DateField(null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name',
                       'last_name', 'img', 'cpf', 'curso', 'data_nasc']

    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name

    def get_img(self):
        return self.img

    def email_user(self, subject, message, from_email=None):
        send_mail(subject, message, from_email, [self.email])
