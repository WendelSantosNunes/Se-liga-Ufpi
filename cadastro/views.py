from conta.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from .forms import UsuarioForm


class UsuarioCreateView(CreateView):
    template_name = 'cadastro/cadastrar.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):

        # Antes do super não foi criado objeto

        url = super().form_valid(form)
        # Profile.objects.create(usuario=self.object)

        # Perfil.object.create(usuario=self.object)

        # Depois do super o objeto está criado
        return url


class UsuarioUpdateView(UpdateView):
    model = User
    template_name = 'cadastro/editar.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('home')
