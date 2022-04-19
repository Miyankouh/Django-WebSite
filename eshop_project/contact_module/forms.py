from django import forms
from .models import ContactUs


class ContactUsForm(forms.Form):
    full_name = forms.CharField(
        label="نام و نام خانوادگی",
        max_length=25,
        error_messages={
            'required': 'لطفا نام و نام خانوادگی خود را وارد کنید',
            'max_length': 'نام و نام خانوادگی نمیتواند بیش از 50 کاراکتر باشد'
        },
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'نام و نام خانوادگی'
        })
    )
    email = forms.EmailField(
        label="ایمیل",
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'ایمیل'
        })
    )
    title = forms.CharField(
        label="عنوان",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'موضوع'
        })
    )
    message = forms.CharField(
        label="متن پیام",
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'متن پیام',
            'rows': '5',
            'id': 'message'
        })
    )


class ContactUsModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['full_name', 'email', 'title', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
                }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '5',
                'id': 'message' 
                })
        }

        labels = {
            'full_name': 'نام و نام خانوادگی شما',
            'email': 'ایمیل شما',
            'title': 'موضوع', 
            'message': 'پیام شما'
        }

        errors = {
            'full_name':{
                'required': 'نام و نام خانوتدگی صحیح نمیباشد'
            }
        }