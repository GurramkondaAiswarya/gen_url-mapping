from django.shortcuts import render

# Create your views here.
def boss(request):
    return render(request,'boss.html')
def employee(request):
    return render(request,'employee.html')