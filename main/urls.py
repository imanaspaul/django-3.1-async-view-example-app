from django.contrib import admin
from django.urls import path
from analyze.views import (
    my_view
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path("analyze/", my_view),
]
