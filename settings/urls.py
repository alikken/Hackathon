from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from csk.views import (
    MainView,
    UserCallView,
    AdminCallView,
    adminpage,
    dashbord,
    profile,
    profile_master,
    
)
from auths.views import (
    LoginViewa,
    RegistrationView,
    LogoutView,
    
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView,),
    path("reg/",RegistrationView.as_view()),
    path("login/",LoginViewa.as_view() ),
    path("logout/",LogoutView.as_view() ),
    path('usercalls/edit/<int:pk>', AdminCallView.as_view(), name='usercalls_edit'),

    path("adminpage/",adminpage,),
    path("callform/",UserCallView.as_view() ),
    # path("callform/",UserCallView),
    path("home/", dashbord),
    # path("profile/", profile),
    path("customer/<str:user_ptr_id>/", profile, name='customer'),
    path("master/<str:user_ptr_id>/", profile_master, name='master'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

