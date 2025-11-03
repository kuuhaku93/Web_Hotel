from django import forms
from .models import Hotel,User

class AddHotel(forms.ModelForm):
    class Meta:
        model=Hotel
        fields=('HotelName','RoomAvilable','Location','Rating','PricePer')
        widgets={
            'HotelName': forms.TextInput(attrs={'id':'HotelName','class':'form-control'}),
            'RoomAvilable': forms.TextInput(attrs={'id':'RoomAvilable','class':'form-control'}),
            'Location': forms.TextInput(attrs={'id':'Location','class':'form-control'}),
            'Rating': forms.NumberInput(attrs={'id':'Rating','class':'form-control'}),
            'PricePer': forms.NumberInput(attrs={'id':'PricePer','class':'form-control'})
        }


class AddUser(forms.ModelForm):
    BookingRoom= forms.ModelChoiceField(queryset=Hotel.objects.filter(RoomAvilable__gt=0,Status=True).distinct(), widget=forms.Select(attrs={'id': 'BookingRoom', 'class': 'form-control'}))
    class Meta:
        model=User
        fields=('UserName','UserID','BookingCost','BookingRoom')
        widgets={
            'UserName': forms.TextInput(attrs={'id':'UserName','class':'form-control'}),
            'UserID': forms.NumberInput(attrs={'id':'UserID','class':'form-control'}),
            'BookingCost': forms.NumberInput(attrs={'id':'BookingCost','class':'form-control'}),
            }