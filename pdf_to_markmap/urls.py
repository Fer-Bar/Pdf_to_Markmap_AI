
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', include('chat_app.urls', namespace='chat_app')),
    path("admin/", admin.site.urls),
    path('logout/', LogoutView.as_view(), name='logout'),
]
