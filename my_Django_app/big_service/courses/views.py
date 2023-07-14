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

def attributes(request):
    template = loader.get_template('attributes.html')
    context = {
        'attributes': ['Omnipotent', 'Omnipresent', 'Omniscient', 'Merciful', 'Impartial', 'Sovereign', 'Provider']
    }
    return HttpResponse(template.render(context, request))

def summary(request):
    mydata = Course.objects.all().values()
    template = loader.get_template('summary.html')
    context = {
        'mycourses': mydata,
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
                'title': 'Extraordinary Attorney Woo', 
                'quote': 'If you have me on your side, you lose. It is better if I am not part of it at all.',
                'year': '2022'
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
