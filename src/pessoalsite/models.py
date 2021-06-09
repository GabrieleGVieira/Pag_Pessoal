from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from autoslug import AutoSlugField
from model_utils.models import TimeStampedModel


class AvailableManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_available=True)


class Quadros(TimeStampedModel):
    title = models.CharField(max_length=255, unique=True,default='null')
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title_quadro01= models.CharField(max_length=255)
    title_quadro02 = models.CharField(max_length=255)
    title_quadro03 = models.CharField(max_length=255)
    description_quadro01 = models.TextField()
    description_quadro03 = models.TextField()
    image_quadro01 = models.ImageField(upload_to='img/',blank=True)
    image_quadro02 = models.ImageField(upload_to='img/',blank=True)
    name_quadro01 = models.CharField(max_length=255,default='null')
    name_quadro02 = models.CharField(max_length=255,default='null')
    name_quadro03 = models.CharField(max_length=255,default='null')
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("pessoalsite:index",kwargs={"slug": self.slug})


class Assuntos(TimeStampedModel):
    aba = models.CharField(max_length=255)
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    
    
   
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("pessoalsite:list_conteudo", kwargs={"slug": self.slug})

class Conteudo(TimeStampedModel):
    assunto = models.ForeignKey(
        Assuntos, related_name="assuntos",on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    identificacao = models.CharField(max_length=255,blank=True)
    title = models.CharField(max_length=255,blank=True)
    cor = models.CharField(max_length=255,blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='img/',blank=True)
    link =  models.CharField(max_length=255,blank=True)
    video = models.CharField(max_length=255,blank=True)
    is_available = models.BooleanField(default=True)

    objects = models.Manager()
    available = AvailableManager()


    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("pessoalsite:list_conteudo", kwargs={"slug": self.assunto})

