from captcha.fields import CaptchaField
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'value': 'Name...', 'onfocus': "this.value='';", 'onblur': "if (this.value=='') {this.value='Name...';}"
    }))
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'value': 'Email...', 'onfocus': "this.value='';", 'onblur': "if (this.value=='') {this.value='Email...';}"
    }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'value': 'Subject...', 'onfocus': "this.value='';", 'onblur': "if (this.value=='') {this.value='Subject...';}"
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'onfocus': "this.value='';", 'onblur': "if (this.value=='') {this.value='Message';}"
    }))
    captcha = CaptchaField()
