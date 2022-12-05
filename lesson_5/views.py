from django.shortcuts import render, get_object_or_404
from lesson_4.models import Author


def index(request):
    return render(request, 'lesson_5/main_3.html')


def search_author(request, name='', surname=''):
    authors = Author.objects.all()
    if 'name' in request.GET:
        name = request.GET['name']
        if name != '':
            authors = authors.filter(name=name)
    if 'surname' in request.GET:
        surname = request.GET['surname']
        if surname != '':
            authors = authors.filter(surname=surname)
    if name == '' and surname == '':
        context = {'searched_authors': authors}
    else:
        context = {'searched_authors': authors}
    return render(request, 'lesson_5/search_author.html', context)
