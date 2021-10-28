"""BusReservation URL Configuration

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
from . import DriverView
from . import BusView
from . import AdminView
from . import SourceView
from . import Booking
from . import UserView

urlpatterns = [
    path('admin/', admin.site.urls),


#DRIVER INTERFACE

    path('driverinterface/',DriverView.DriverInterface),
    path('submitdriverrecord',DriverView.SubmitDriverRecord),
    path('displayalldriver/',DriverView.DisplayAllDriver),
    path('displaydriverbyid/',DriverView.DisplayDriverbyid),
    path('editdeletedriverrecord/',DriverView.EditDeleteDriverRecord),

#BusInterface

    path('businterface/',BusView.BusInterface),
    path('submitbusrecord',BusView.SubmitBusRecord),
    path('displayallbus/',BusView.DisplayAllBus),
    path('fetchcityjason/',BusView.FetchCityJason),
    path('displaybusbyid/',BusView.DisplayBusbyid),
    path('editdeletebusrecord/',BusView.EditDeleteBusRecord),


#Admin

    path('admindashboard/',AdminView.AdminDashboard),
    path('adminlogin/',AdminView.AdminLogin),
    path('checkadminlogin',AdminView.CheckAdminLogin),
    path('adminlogout/',AdminView.AdminLogout),

#Source

    path('sourcedestination/',SourceView.SourceDestination),
    path('displaysearchbus/',SourceView.DisplaySearchBus),


#Booking

    path('bookingticket/',Booking.BookingTicket),
    path('bookticket/',Booking.BookTicket),
    path('submitbookingrecord/',Booking.SubmitBookingRecord),
    path('displayallbooking/',Booking.DisplayAllBooking),
    path('showmyticket/',Booking.ViewTicket),

#User

    path('aboutus/',UserView.AboutUs),
    path('contactus/',UserView.ContactUs),
    path('index/',UserView.Index),




]
