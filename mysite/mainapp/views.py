from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/includes/homepage.html')


def contact(request):
    return render(request, 'mainapp/base.html', {'values': ['По всем вопросам: ', '(099)-999-99-99', 'email@gmail.com']})
