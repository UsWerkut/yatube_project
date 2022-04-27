from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def all_groups(request):
    return HttpResponse('Все группы YaTube')


def group_posts(request, slug):
    return HttpResponse(f'Группа YaTube: {slug}')
