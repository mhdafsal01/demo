from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('opr/', views.opr, name='opr'),
    # path('login/', views.login, name='login'),
    # path('thanks/',views.thanks,name='login')

]
