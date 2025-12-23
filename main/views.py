from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import *

def home_view(request):
    students = Student.objects.all()
    return render(request, 'home.html')

def students_view(request):
    students = Student.objects.all()
    kursi = Student.objects.filter(kurs=3)

    context = {
        'students': students,
        'kursi': kursi
    }
    return render(request, 'student.html', context)


def plans_view(request):
    plans = Reja.objects.all()
    bajarilmaga = Reja.objects.filter(bajarildi=False)
    context = {'plans': plans,
            'bajarilmaga': bajarilmaga
               }
    return render(request, 'plans.html', context)

def plans_delete_view(request, plan_id):
    plan = Reja.objects.get(id=plan_id)
    plan.delete()
    return redirect('/plans/')
