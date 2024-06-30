from django.shortcuts import render
from django.views import View


from . import forms


class UserRegisterView(View):

    form_class = forms.UserRegitrationForm

    def get(self, request):
        form = self.form_class
        return render(request, 'accounts/register.html', {'form': form})

    def post(self, request):
        pass
