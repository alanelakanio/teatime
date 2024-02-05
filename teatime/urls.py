# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('teatime_app/', include('teatime_app.urls')),  # Include app URLs
]
