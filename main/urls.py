from django.urls import path

from .views import HomeView, Pesquisa, about, post

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('sobre/', about, name="sobre"),
    path('pesquisa/', Pesquisa.as_view(), name="pesquisa"),
    path('post/<int:pk>', post, name="postagem"),
]
