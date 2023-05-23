from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text',)
        widgets = {
            'name':forms.TextInput(attrs={
                'type':'text',
                'placeholder':'Your name'
            }),
            'email':forms.TextInput(attrs={
                'type':'text',
                'placeholder':'E-Mail Adress',
            }),
            'text':forms.Textarea(attrs={
                'placeholder':'Morbi leo risus, porta ac consectetur ac, vestibulum at eros.'
            })
            
        }