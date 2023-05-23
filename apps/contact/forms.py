from django.forms import ModelForm, TextInput, Textarea

from .models import ContactModelForm


class ContactForm(ModelForm):
    class Meta:
        model = ContactModelForm
        fields = '__all__'
        widgets = {
            'name':TextInput(attrs={
                'type':'text',
                'id':'cname',
                'name':'name',
                'placeholder':'Name',
                'style':'margin-top:80px;'
            }),
            'email':TextInput(attrs={
                'type':'text',
                'id':'cmail',
                'name':'email',
                'placeholder':'E-mail'
            }),
            'description':Textarea(attrs={
                'id':'ctext',
                'name':'message',
                'placeholder':'Write what do you want...'
            })
        }