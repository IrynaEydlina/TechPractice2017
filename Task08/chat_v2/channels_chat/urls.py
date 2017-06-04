"""channels_chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from channels_chat import settings
from django.conf import settings

urlpatterns = [
    url(r'^', include('chat.urls', namespace='chat')),
    url(r'^admin/', admin.site.urls),
    url(r'^users/', include('users.urls', namespace='users')),
    url(r'^chat/', include('chat.urls', namespace='chat')),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    url('', include('social_django.urls', namespace='social')),# <--
    url("^soc/", include("social_django.urls", namespace="social")),
    url('', include('django.contrib.auth.urls', namespace='auth')),    
 url(r'social/',
        include('social.apps.django_app.urls', namespace='social')),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

