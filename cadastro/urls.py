from django.urls import path

from .views import UpdateView, UsuarioCreateView, UsuarioUpdateView

urlpatterns = [
    path('', UsuarioCreateView.as_view(), name="cadastrar"),
    path('editar/<int:pk>', UsuarioUpdateView.as_view(), name="editar"),
]
