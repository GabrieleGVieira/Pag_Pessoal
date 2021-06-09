
from django.views.generic import DetailView, ListView
from .models import Conteudo, Quadros,Assuntos
from django.shortcuts import get_object_or_404
from django.shortcuts import render



class QuadrosListView(ListView):
    
    quadros = None

    def get_queryset(self):
        queryset = Quadros.objects.all()

        quadros_slug = self.kwargs.get("slug")
        if quadros_slug:
            self.quadros = get_object_or_404(Quadros, slug=quadros_slug)
            queryset = queryset.filter(title=self.quadros)

        return queryset

    def get_context_data(self, **kwargs):
        context_quadros = super().get_context_data(**kwargs)
        context_quadros["quadro"] = self.quadros
        context_quadros["quadros"] = Quadros.objects.all()
        
        return context_quadros
         
class ConteudoListView(ListView):
    assunto = None

    def get_queryset(self):
        queryset = Conteudo.available.all()

        assunto_slug = self.kwargs.get("slug")
        if assunto_slug:
            self.assunto = get_object_or_404(Assuntos, slug=assunto_slug)
            queryset = queryset.filter(assunto=self.assunto)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["assunto"] = self.assunto
        context["assuntos"] = Assuntos.objects.all()
      
        
        return context





# Create your views here.
