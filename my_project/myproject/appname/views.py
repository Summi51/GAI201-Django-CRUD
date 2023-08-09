from django.shortcuts import render
from django.http import HttpResponse


data = {"name": "Samreen Inayat",  "age": 23, "course" : "Masai", "city": "Pratapgarh", "gender": "Female", "state:": "Uttar Pradesh"}

#post - create
def create(request):
    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        data[key] = value
    return render(request, "create.html")


# Delete 
def delete(request):
    if request.method == "POST":
        key = request.POST.get("key")
        if key in data:
            del data[key]
    return render(request, "delete.html", {"data": data})

# get
def read(request):
    return render(request, "read.html", {"data": data})



#update - edit
def update(request):
    if request.method == "POST":
        key = request.POST.get("key")
        value = request.POST.get("value")
        if key in data:
            data[key] = value
    return render(request, "update.html", {"data": data})

