from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from lesson_4.models import Author
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm


class MainView(TemplateView):
    template_name = 'lesson_7/main_7.html'

    def get(self, request):
        if request.user.is_authenticated:
            authors = Author.objects.all()
            context = {'authors': authors}
            return render(request, self.template_name, context)
        else:
            return render(request, self.template_name, {})


class RegisterFormView(FormView):
    form_class = UserCreateForm
    success_url = '/lesson_7/login/'

    template_name = 'lesson_7/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)


class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'lesson_7/login.html'
    success_url = '/lesson_7/'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/lesson_7/')
