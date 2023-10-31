# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Course

def courses(request):
    mycourses = Course.objects.all().values()
    template = loader.get_template('all_courses.html')
    context = {
        'mycourses': mycourses,
    }
    return HttpResponse(template.render(context, request))

def details(request, id):
    mycourse = Course.objects.get(id=id)
    template = loader.get_template('details.html')
    context = {
        'mycourse': mycourse,
    }
    return HttpResponse(template.render(context, request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())

def summary(request):
    mydata = Course.objects.all().values()
    template = loader.get_template('summary.html')
    context = {
        'mycourses': mydata,
    }
    return HttpResponse(template.render(context, request))

def bookmarks(request):
    template = loader.get_template('bookmarks.html') # attributes
    context = {
        'bookmarks': [
            {
                'site': 'Kim, Chang-ok FourFreeShow',
                'url': 'https://www.youtube.com/4freeshow/videos',
            },
            {
                'site': 'Cats and Kittens vlog',
                'url': 'https://www.youtube.com/@MeowsRUs',
            },
            {
                'site': 'You are Special ',
                'url': 'https://www.youtube.com/watch?v=I7UnyVhHGD0',
            },
            {
                'site': 'Bellevue College WE ',
                'url': 'https://www.bellevuecollege.edu/we',
            },
            {
                'site': 'XPress engine ',
                'url': 'https://github.com/xpressengine/xe-core',
            },
        ]
    }
    return HttpResponse(template.render(context, request))

def quotes(request):
    template = loader.get_template('quotes.html')
    context = {    
        'quotes': [
            {
                'title': 'Agency',
                'quote': 'A swan incessantly kicks its legs beneath the surface.',
                'year': '2023',
            },
            {
                'title': 'Agency',
                'quote': 'Think strategically and act crazy.', 
                'year': '2023',
            },
            {
                'title': 'Anne of Green Gables', 
                'quote': 'God is in his heaven, all is right with the world.',
                'year': '2020'
            },
            {
                'title': 'Anne of Green Gables',
                'quote': 'It\'s been my experience that you can nearly always enjoy things if you make up your mind firmly that you will.',
                'year': '1908'
            },
            {
                'title': 'Extraordinary Attorney Woo', 
                'quote': 'The thread and the needle were fighting. The police arrested the thread because the needle sewed the thread.',
                'year': '2022'
            },
            {
                'title': 'Ecclesiastes 3:1', 
                'quote': 'There is a time for everything, and a season for every activity under heaven.',
                'year': 'B.C. 950'
            },
        ]
    }
    return HttpResponse(template.render(context, request))
