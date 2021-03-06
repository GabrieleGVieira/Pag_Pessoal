# Generated by Django 3.1.3 on 2021-06-06 00:34

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Assuntos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Quadros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField( max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('title_quadro01', models.CharField(max_length=255)),
                ('title_quadro02', models.CharField(max_length=255)),
                ('title_quadro03', models.CharField(max_length=255)),
                ('description_quadro01', models.TextField()),
                ('description_quadro03', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Conteudo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='assunto')),
                ('identificacao', models.CharField(blank=True, max_length=255, unique=True)),
                ('title', models.CharField(blank=True, max_length=255)),
                ('cor', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='static/img/')),
                ('link', models.CharField(blank=True, max_length=255)),
                ('video', models.CharField(blank=True, max_length=255)),
                ('is_available', models.BooleanField(default=True)),
                ('assunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assuntos', to='pessoalsite.assuntos')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='assuntos',
            name='aba',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quadros', to='pessoalsite.quadros'),
        ),
    ]
