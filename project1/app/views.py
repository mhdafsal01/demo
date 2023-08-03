from django.http import HttpResponse
from django.shortcuts import render
from .models import Place, Team


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    obj0 = Team.objects.all()
    return render(request, "index.html", {'result': obj, 'team': obj0})

# def opr(request):
#     x = int(request.GET['n1'])
#     y = int(request.GET['n2'])
#     addr = x + y
#     subr = x - y
#     mulr = x * y
#     divr = x / y
#     return render(request, "result.html", {'add': addr, 'sub': subr, 'mul': mulr, 'div': divr})

# def login(request):
#     return render(request, "login.html")
#
# def thanks(request):
#     return HttpResponse("thanks for visiting")
