from django import forms
from django.forms import ModelForm

from .models import *
from apps.hoteInfo.models import NewSteller


class OrderForm(ModelForm):
    class Meta:
        model = BookNow
        fields = '__all__'
        
        widgets = {
            'comnat' : forms.Select(attrs={
                                            'style':'color:black; background-color:white; width:550px;',
                                            'class':"pretty-select "

                                                }),
            'arrivial': forms.DateInput(attrs={
                                                'type':"text" ,
                                                'id':"dpd1" ,
                                                'name':"dpd1" ,
                                                'data-date-format':"dd/mm/yyyy" ,
                                                'class':"date-selector",
                                                'autocomplete':'off'
                                               }),
            'departure': forms.DateInput(attrs={
                                                'type':"text" ,
                                                'id':"dpd2" ,
                                                'name':"dpd2" ,
                                                'data-date-format':"dd/mm/yyyy" ,
                                                'class':"date-selector",
                                                'autocomplete':'off'
                                               }),
            'rooms': forms.Select(attrs={
                                        'name':"rooms" ,
                                        'class':"pretty-select"
                                        }),

            'adult': forms.Select(attrs={
                                        'name':"adult" ,
                                        'class':"pretty-select"
                                    }),
            'children': forms.Select(attrs={
                                        'name':"children" ,
                                        'class':"pretty-select"
                                    }),
            'email':forms.TextInput(attrs={
                
            }),
            'phone':forms.TextInput(attrs={
                
            })
            
            
        }


class NewStellerForm(ModelForm):
    class Meta:
        model = NewSteller
        fields = '__all__'
        widgets = {
            'email':forms.TextInput(attrs={
                'placeholder':'Enter a e-mail address',
                'style':'display:inline-block;'
            })
        }
