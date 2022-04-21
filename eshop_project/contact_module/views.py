from django.shortcuts import redirect, render
from django.views import View
from django.views.generic import CreateView, FormView
from .forms import  ContactUsModelForm, ProfileForm
from .models import ContactUs, UserProfile


class ContactUsView(CreateView):
    form_class = ContactUsModelForm
    template_name = 'contact_module/contact_us_page.html'
    success_url = '/contact-us/'


def store_file(file):
    with open('temp/image.jpg', "wb+") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    

class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, 'contact_module/create_profile_page.html', {
            'form': form
        })

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            # store_file(request.FILES['profile'])
            profile = UserProfile(image=request.FILES['user_image'])
            profile.save()
            return render(request, 'contact_module/create_profile_page.html')
        
        return render(request, 'contact_module/create_profile_page.html', {
            'form': submitted_form
        })


        