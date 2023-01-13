from django.urls import path #path cria as rotas, as urls
# da pasta que eu estou importe o arquivo views. O ponto quer dizer que é do local em que estiver.
from . import views # views -> arquivo onde é localizado as funções do python responsavel por processar os dados

urlpatterns = [
    path('cadastro/', views.cadastro, name="cadastro"),
    path('login/', views.logar, name="login"),
    path('sair/', views.sair, name="sair"),
]