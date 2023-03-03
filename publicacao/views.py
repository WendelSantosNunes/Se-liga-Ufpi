import json

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.
from .forms import PublicarForm
from .models import Publicacao


class PublicarCreate(LoginRequiredMixin, CreateView):
    success_url = reverse_lazy('home')
    template_name = 'publicacao/publicacao.html'
    form_class = PublicarForm

    def form_valid(self, form):

        form.instance.usuario = self.request.user
        form.instance.denuncia = 0

        # Antes do super não foi criado objeto

        url = super().form_valid(form)

        # Depois do super o objeto está criado
        return url


class UpdatePublicacaoView(UpdateView):
    model = Publicacao
    form_class = PublicarForm
    template_name = 'publicacao/publicacao-editar.html'
    success_url = reverse_lazy('home')


class DeleteViewPublicacaoView(DeleteView):
    model = Publicacao
    template_name = 'publicacao/form-excluir.html'
    success_url = reverse_lazy('home')


def BlogPostLike(request, pk):
    print(request, pk)

    post = get_object_or_404(Publicacao, id=pk)

    action = json.loads(request.body)

    print(request.user.id)

    print(post.usuario_id)

    print(post.euvou.filter(id=pk).exists())

    print(action['action'], action)
    if (post.usuario_id != request.user.id):
        if action['action'] == 'euvou':
            if post.euvou.filter(id=request.user.id).exists():
                post.euvou.remove(request.user)
            else:
                if post.topensando.filter(id=request.user.id).exists():
                    post.topensando.remove(request.user)
                post.euvou.add(request.user)
        else:
            if post.topensando.filter(id=request.user.id).exists():
                post.topensando.remove(request.user)
            else:
                if post.euvou.filter(id=request.user.id).exists():
                    post.euvou.remove(request.user)
                post.topensando.add(request.user)

    resposta1 = post.number_of_euvou()
    resposta2 = post.number_of_topensando()

    if post.euvou.filter(id=request.user.id).exists():
        euvou = True
    else:
        euvou = False

    if post.topensando.filter(id=request.user.id).exists():
        topensando = True
    else:
        topensando = False

    dictonary = {
        'value1': resposta1,
        'value2': resposta2,
        'existe_euvou': euvou,
        'existe_topensando': topensando
    }

    json_object = json.dumps(dictonary)
    return HttpResponse(json_object, content_type="application/json")
