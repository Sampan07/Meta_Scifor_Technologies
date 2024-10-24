from django.shortcuts import render

# Create your views here.
def bye(request):
    return render(request,'bye/bye.html')