from django.shortcuts import render

# Create your views here.


def search_crime_in_place(request):
    return render(request,'auth/home.html')
