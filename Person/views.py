from django.shortcuts import render, redirect
from .models import Person

# Create your views here.


def list_persons(request):
    persons = Person.objects.all()
    context = {"persons": persons}
    return render(request, "index.html", context)


def create_person(request):
    person = Person(
        name=request.POST["name"],
        last_name=request.POST["last_name"],
        age=request.POST["age"],
        birthday=request.POST["birthday"],
    )
    person.save()
    return redirect("/person/")

def delete_person(request, id):
    person = Person.objects.get(id=id)
    person.delete()
    return redirect("/person/")