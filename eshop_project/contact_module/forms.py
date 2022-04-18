from django import forms


class ContactUsForm(forms.Form):
    fullname = forms.CharField()
    email = forms.EmailField()
    subject = forms.CharField()
    text = forms.CharField()

