from django import forms
from .models import Car

class CarModelForm(forms.ModelForm):
    make = forms.CharField(label="",widget=forms.TextInput(attrs = {'placeholder':"Make",'class': "TextInput"}))
    Type = forms.CharField(label="",widget=forms.TextInput(attrs = {'placeholder':"Type",'class': "TextInput"}))
    year = forms.CharField(label="",widget=forms.TextInput(attrs = {'placeholder':"year",'class': "TextInput"}))
    colour = forms.CharField(label="",widget=forms.TextInput(attrs = {'placeholder':"colour",'class': "TextInput"}))
    price= forms.CharField(label="",widget=forms.TextInput(attrs = {'placeholder':"price",'class': "TextInput"}))
    image = forms.FileField()
    #created = forms.CharField(label="",widget=forms.TextInput(attrs = {'placeholder':"created",'class': "TextInput"}))

    class Meta:
        model = Car
        fields= ["make","Type","year","colour","price","image",]
