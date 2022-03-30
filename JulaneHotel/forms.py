from django import forms
from .models import *

class RoomsForm(forms.ModelForm):

    class Meta:
            model = Rooms
            fields= "__all__"


class CustomerForm(forms.ModelForm):

    class Meta:
            model = Customer
            fields= "__all__"

class ReservationForm(forms.ModelForm):

    class Meta:
            model = Reservation
            fields= "__all__"

class AdminForm(forms.ModelForm):

    class Meta:
            model = Admin
            fields= "__all__"