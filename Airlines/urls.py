"""MyAirlines URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from MyAirlines import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.MyHome),
    path('login/',views.MyLogin),
    path('signup/',views.MySignup),
    path('adash/',views.AdminDash),
    path('udash/',views.UserDash),
    path('fadd/',views.FlightAdd),
    path('flight/',views.FlightPage),
    path('custviews/',views.CustView),
    path('res/',views.Reservation),
    path('resview/',views.RevView),
    path('adminresview/',views.AdminRevView),
    path('revcancel/',views.RevCancel),
    path('arevcancel/',views.AdminRevcancel),
    path('adminrevdel/',views.AdminRevDel),

]
