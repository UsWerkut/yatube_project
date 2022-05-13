from re import template
from turtle import title
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'base.html'
    title = 'YaTube'
    text = 'Это главная страница проекта Yatube'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, template, context)


def all_groups(request):
    return HttpResponse('Все группы YaTube')


def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'YaTube'
    text = 'Здесь будет информация о группах проекта Yatube '
    context = {
        'title': title,
        'text': text,
    }

    return render(request, template, slug, context)
