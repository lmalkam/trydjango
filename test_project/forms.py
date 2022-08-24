from socket import fromshare
from django import forms 

class ContactForm(forms.Form):
    full_name = forms.CharField()
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    publish_date = forms.DateField()