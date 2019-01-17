from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import TestText
from django.db.models import Q

@login_required
def exams(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Obecné")[:1]
    my_total = TestText.objects.filter(tag="Obecné").count()
    return render(request, 'exams/Exam1.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam2(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Živnostenský zákon")[:1]
    my_total = TestText.objects.filter(tag="Živnostenský zákon").count()
    return render(request, 'exams/Exam2.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam3(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Silniční doprava")[:1]
    my_total = TestText.objects.filter(tag="Silniční doprava").count()
    return render(request, 'exams/Exam3.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam4(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Provozní řád stanovišť taxi")[:1]
    my_total = TestText.objects.filter(tag="Provozní řád stanovišť taxi").count()
    return render(request, 'exams/Exam4.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam5(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Pravidla silničního provozu")[:1]
    my_total = TestText.objects.filter(tag="Pravidla silničního provozu").count()
    return render(request, 'exams/Exam5.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam6(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Pojištění odpovědnosti ")[:1]
    my_total = TestText.objects.filter(tag="Pojištění odpovědnosti ").count()
    return render(request, 'exams/Exam6.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam7(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Kontrolní řád")[:1]
    my_total = TestText.objects.filter(tag="Kontrolní řád").count()
    return render(request, 'exams/Exam7.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam8(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Ceny")[:1]
    my_total = TestText.objects.filter(tag="Ceny").count()
    return render(request, 'exams/Exam8.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam9(request):
    random_obj = TestText.objects.all().order_by('?').filter(jeLegislativa="True")[:1]
    my_total = TestText.objects.filter(jeLegislativa="True").count()
    return render(request, 'exams/Exam9.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam10(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Určení adres objektů")[:1]
    my_total = TestText.objects.filter(tag="Určení adres objektů").count()
    return render(request, 'exams/Exam10.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam11(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Orientační vzdálenost")[:1]
    my_total = TestText.objects.filter(tag="Orientační vzdálenost").count()
    return render(request, 'exams/Exam11.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam12(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Trasy")[:1]
    my_total = TestText.objects.filter(tag="Trasy").count()
    return render(request, 'exams/Exam12.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam13(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Organizace dopravy")[:1]
    my_total = TestText.objects.filter(tag="Organizace dopravy").count()
    return render(request, 'exams/Exam13.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam14(request):
    random_obj = TestText.objects.all().order_by('?').filter(tag="Určení polohy ulice (náměstí)")[:1]
    my_total = TestText.objects.filter(tag="Určení polohy ulice (náměstí)").count()
    return render(request, 'exams/Exam14.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def Exam15(request):
    random_obj = TestText.objects.all().order_by('?').filter(jeLegislativa="False")[:1]
    my_total = TestText.objects.filter(jeLegislativa="False").count()
    return render(request, 'exams/Exam15.html',{'random_obj':random_obj, 'my_total':my_total})

@login_required
def searchTest(request):
    return render(request, 'exams/SearchTest.html', {})
