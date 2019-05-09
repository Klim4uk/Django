from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/homepage.html')


def contact(request):
    return render(request, 'mainapp/basic.html', {'values': ['По всем вопросам: ', '(099)-999-99-99', 'email@gmail.com']})
