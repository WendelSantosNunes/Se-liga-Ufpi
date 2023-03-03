from django.urls import path

from .views import (BlogPostLike, DeleteViewPublicacaoView, PublicarCreate,
                    UpdatePublicacaoView)

urlpatterns = [
    path('', PublicarCreate.as_view(), name="publicacao"),
    path('editar/<int:pk>', UpdatePublicacaoView.as_view(),
         name="editar-publicacao"),
    path('excluir/<int:pk>', DeleteViewPublicacaoView.as_view(),
         name="excluir-publicacao"),
    path('blogpost-like/<int:pk>', BlogPostLike, name="blogpost_like"),
    #     path('like/<int:idpost>/<int:intencao>', Acoes, name='acoes')
]
