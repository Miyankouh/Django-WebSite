from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, FormView, ListView
from .forms import  ContactUsModelForm
from .models import ContactUs, UserProfile
from site_module.models import SiteSetting


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
        context['site_setting'] = setting
        return context


def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile_page.html'
    model = UserProfile
    fields='__all__'
    success_url = '/contact-us/create-profile'


class ProfileView(ListView):
    model = UserProfile
    template_name = 'contact_module/profile_list_page.html'
    context_object_name = 'profiles'
    