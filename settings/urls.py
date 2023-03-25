from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from csk.views import (
    MainView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainView.as_view()),
]
