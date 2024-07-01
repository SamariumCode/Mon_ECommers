import random
from django.views import View
from django.shortcuts import render, redirect
from django.contrib import messages

from utils import send_otp_code
from . models import OtpCode
from . import forms


class UserRegisterView(View):

    form_class = forms.UserRegitrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(
                phone_number=form.changed_data['phone'], code=random_code)
            request.session['user_registration_info'] = {
                'phone_number': form.cleaned_data['phone'],
                'email': form.changed_data['email'],
                'full_name': form.changed_data['full_name'],
                'password': form.cleaned_data['password']
            }
            messages.success(
                request, 'ما کدی رو برای شما ارسال کردیم', extra_tags='success')
            return redirect('accounts:verify_code')
        return redirect('home:home')


class UserRegisterVerifyCodeView(View):

    def get(self, request):
        pass

    def post(self, request):
        pass
