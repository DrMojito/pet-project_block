from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    context = {
        'title': "Главная страница"
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    context = {
        'title': "Здесь информация о мороженном}"
    }
    return render(request, template, context)