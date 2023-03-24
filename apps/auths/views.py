from django.shortcuts import render, redirect
from django.http import (
    HttpRequest, 
    HttpResponse
)
from django.db.models import QuerySet
from django.views.generic import View
from django.forms.models import ModelFormMetaclass
from django.core.handlers.wsgi import WSGIRequest
from django.contrib.auth import (
    login, 
    logout,
    authenticate
)
from django.contrib.auth.hashers import make_password

# Local
from csk.models import MasterUser
from auths.models import CustomUser
from abstracts.mixins import HttpResponseMixin
from auths.forms import (
    RegistrationForm,
    LoginForm
)


class RegistrationView(HttpResponseMixin, View):
    """Registration View."""

    template_name = 'auths/registration.html'
    form: ModelFormMetaclass = RegistrationForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        return self.get_http_response(
            request=request,
            template_name=self.template_name,
            context={
                'ctx_form': self.form()
            }
        )

    def post(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        form: RegistrationForm = self.form(
            request.POST
        )
        if not form.is_valid():
            return HttpResponse("BAD")

        custom_user: CustomUser = form.save(
            commit=False
        )
        custom_user.password =\
            make_password(custom_user.password)

        custom_user.save()
        return HttpResponse("OK")


class LoginView(HttpResponseMixin, View):
    """Login View."""

    template_name: str = 'auths/login.html'
    form: ModelFormMetaclass = LoginForm

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
    ) -> HttpResponse:
        return self.get_http_response(
            request=request,
            template_name=self.template_name,
            context={
                'ctx_title' : 'Login',
                'ctx_form' : self.form()
            }
        )

    def post(
         self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict,
    ) -> HttpResponse:
        form: LoginForm = self.form(
            request.POST
        )
        if not form.is_valid():
            return self.get_http_response(
                request=request,
                template_name=self.template_name,
                context={
                    'ctx_title' : 'Login',
                    'ctx_form' : self.form()
                }
            )

        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user: CustomUser = authenticate(
            username=email,
            password=password
        )
        if not user:
            return self.get_http_response(
                request=request,
                template_name=self.template_name,
                context={
                    'ctx_title' : 'Error',
                    'ctx_form' : self.form()
                }
            )

        login(request, user)

        return redirect('/')


class LogoutView(HttpResponseMixin, View):
    """LogoutView."""

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        if request.user:
            logout(request)
        
        return redirect('/')


class ProfileView(HttpResponseMixin, View):
    """ProfileView."""

    template_name: str = "auths/profile.html"

    def get(
        self,
        request: WSGIRequest,
        *args: tuple,
        **kwargs: dict
    ) -> HttpResponse:
        
        return self.get_http_response(
            request=request,
            template_name=self.template_name,
            context={
                "ctx_user": request.user
            }
        )
    
    