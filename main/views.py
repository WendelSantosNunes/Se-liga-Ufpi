
import json
from datetime import date
from pprint import pprint

from django.shortcuts import get_object_or_404, render
from django.views.generic.list import ListView
from publicacao.models import Publicacao

today = date.today()


class HomeView(ListView):
    model = Publicacao
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        array = Publicacao.objects.values()

        context['pesquisa'] = []

        for publicacao in array:
            post = get_object_or_404(Publicacao, id=publicacao['id'])

            if int((post.data_evento - today).days) > 0:
                publicacao['valorEuvou'] = post.number_of_euvou()
                context['pesquisa'].append(publicacao)

        if len(context['object_list']) > 0:
            enddate = context['object_list'].values(
                'data_evento').order_by('-data_evento')[0]

            context['object_list'] = context['object_list'].filter(
                data_evento__range=[today, enddate['data_evento']])

        context['pesquisa'] = sorted(
            context['pesquisa'], key=lambda k: k['valorEuvou'], reverse=True)

        context['pesquisa'] = context['pesquisa'][:4]

        return context


def about(request):
    return render(request, 'sobre/sobre.html')


def post(request, pk):

    post = get_object_or_404(Publicacao, id=pk)

    return render(request, 'postagem/post.html', {"post": post})


class Pesquisa(ListView):
    model = Publicacao
    template_name = "main/home.html"

    def get_context_data(self, **kwargs):
        context = super(Pesquisa, self).get_context_data(**kwargs)
        array = Publicacao.objects.values()
        context['pesquisa'] = []

        for publicacao in array:
            post = get_object_or_404(Publicacao, id=publicacao['id'])

            if int((post.data_evento - today).days) > 0:
                publicacao['valorEuvou'] = post.number_of_euvou()
                context['pesquisa'].append(publicacao)

        if len(context['object_list']) > 0:
            enddate = context['object_list'].values(
                'data_evento').order_by('-data_evento')[0]

            context['object_list'] = context['object_list'].filter(
                data_evento__range=[today, enddate['data_evento']]).order_by('data_evento')

        context['pesquisa'] = sorted(
            context['pesquisa'], key=lambda k: k['valorEuvou'], reverse=True)

        context['pesquisa'] = context['pesquisa'][:4]
        return context


# class Passados(ListView):
#     model = Publicacao
#     template_name = "main/home.html"

#     def get_context_data(self, **kwargs):
#         context = super(HomeView, self).get_context_data(**kwargs)
#         array = Publicacao.objects.values()

#         context['pesquisa'] = array[:4]

#         enddate = context['object_list'].values(
#             'data_evento').order_by('-data_evento')[0]

#         context['object_list'] = context['object_list'].filter(
#             data_evento__range=[today, enddate['data_evento']]).order_by('-data_evento')

#         return context
