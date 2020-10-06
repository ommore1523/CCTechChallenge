from django import forms
from .models import Gallery

#Django model form 
class Gallery_form(forms.ModelForm):
    class Meta:
        model = Gallery
        fields=['photo']
        widgets = {
        'photo': forms.FileInput(attrs={'name':'file' ,'class':'inputfile' ,'onchange':'yourFunction()','id':'file'}),
         }
