# Python
from typing import Any
from urllib import request

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.db.models import QuerySet
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.http import (
    HttpRequest,
    HttpResponse,
    QueryDict,
)
from django.views.generic import (
    View,
    ListView,
)

from django.views.generic.edit import UpdateView

from django.core.files.uploadedfile import InMemoryUploadedFile

# Local
from .models import (
    UserCall,
    MasterUser
)
from .forms import (
    UserCallForm,
    UserCallUpdateForm,
    UserCallForm2
)
from abstracts.mixins import HttpResponseMixin
# from .forms import (
#     UserCallForm,
# )


class MainView(HttpResponseMixin, View):
    """Main view."""

    def get(self, request: HttpRequest, *args, **kwargs):

        return self.get_http_response(
            request=request,
            template_name='home_page.html',
            context={
                'ctx_user': request.user
            }
        )
    
# @login_required
# def UserCallView(request):
#     if request.method == 'POST':
#         form = UserCallForm(request.POST)
#         if form.is_valid():
            
#             order = form.save(commit=False)
#             order.caller = request.user
#             order.save()
#             return redirect('/')
            
#     else:
#         form = UserCallForm()
#     return render(request, 'main/callform.html', {'ctx_form': form})
class UserCallView(HttpResponseMixin,View):
    """View for UserCall."""
    
    form = UserCallForm

    def get(self, request: HttpRequest, *args: tuple, **kwargs: dict):
        return self.get_http_response(
            request=request,
            template_name='main/callform.html',
            context={
                'ctx_form' : self.form()
            }
        )

    def post(self, request,*args: tuple,  **kwargs: dict):
        if request.method == 'POST':
            print("sdfsdfsdfs", request.POST)
            form = UserCallForm2(request.POST)
            if form.is_valid():
                print("8888888888888888888888888888888888888888888888888")
                order = form.save(commit=False)
                order.caller = request.user
                order.save()
                return redirect('/')
            else:
                print(form.errors)
                return self.get_http_response(
                    request=request,
                    template_name='main/callform.html',
                    context={
                        'ctx_form' : form
                    }
                )


class AdminCallView(UpdateView):
    """Admin redact calls."""

    template_name = "admin/usercall_edit.html"
    model = UserCall
    form_class = UserCallUpdateForm

    def get_success_url(self):
        return "/callform/"
    
    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        masterr = MasterUser.objects.get(id=request.POST.get('caller'))
        masterr.is_busy = True
        masterr.save()
        return super(AdminCallView,self).post(request, *args, **kwargs)


def adminpage(request):
    callforms=UserCall.objects.all()
    # customers=CustomUser.objects.all()
    context={"callforms":callforms,}
    return render(request,'admin/adminpage.html', context )  



def dashbord(request):
    return render(request, 'dashbord/dashbord_main.html')

def profile(request):
    return render(request, "profile_user/profile.html")