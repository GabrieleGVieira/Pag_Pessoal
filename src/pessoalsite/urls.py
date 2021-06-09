from django.urls import path





from .views import  ConteudoListView,QuadrosListView

app_name = 'pessoalsite'

urlpatterns = [
    path("<slug:slug>/", QuadrosListView.as_view(), name='index'),
    path("conteudo/<slug:slug>/", ConteudoListView.as_view(), name='list_conteudo'),

    ]
