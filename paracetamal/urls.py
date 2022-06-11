from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login_view', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('consulta_interacoes', views.consulta_interacoes, name='consulta_interacoes'),
    path('integrantes_grupo', views.integrantes_grupo, name='integrantes_grupo'),
    path('autocomplete_busca_componente', views.autocomplete_busca_componente, name='autocomplete_busca_componente'),
]
