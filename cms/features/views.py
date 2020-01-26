from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def addCourse(request):
    if request.method == "POST":
        course_name = request.POST["course_name"]
        course_code = request.POST["course_code"]
        course_details =request.POST["course_details"]
        course_date = request.POST["course_date"]
        course_price = request.POST["course_price"]
        professor_name = request.POST["professor_name"]
        max_stud = request.POST["max_stud"]
        contact_number = request.POST["contact_number"]
        c = Courses(course_name=course_name, course_code=course_code, course_details=course_details, course_date=course_date, course_price=course_price, professor_name=professor_name, maximum_students=max_stud, contact_number=contact_number)
        c.save();
        return render(request, "viewcourse.html")

    return render(request, "addcourse.html")

def viewCourse(request):
    return render(request, "viewcourse.html")

def viewLibrary(request):
    return render(request, "viewlibrary.html")

def addLibrary(request):
    return render(request, "addlibrary.html")

def addEvent(request):
    return render(request, "addevents.html")

def viewEvent(request):
    return render(request, "viewevents.html")

def addFees(request):
    return render(request, "addfees.html")

def viewFees(request):
    return render(request, "viewfees.html")