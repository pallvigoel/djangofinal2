"""mysite URL Configuration

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
import allauth

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from profiles import views as profiles_views
from contact import views as contact_views
from polls import views as polls_views
from polls import views as details_views
from polls import views as new_views
from polls import views as edit_views
from polls import views as core_views
from django.views.generic.base import TemplateView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', profiles_views.home, name='home'),
    url(r'^about/$', profiles_views.about, name='about'),
    url(r'^contact/$', contact_views.contact, name='contact'),
    
    url(r'^polls/$', polls_views.post_list, name='post_list'),
    url(r'^polls/(?P<pk>\d+)/$',details_views .post_detail, name='post_detail'),
    url(r'^polls/new/$', new_views.post_new, name='post_new'),
    url(r'^polls/(?P<pk>\d+)/edit/$', edit_views.post_edit, name='post_edit'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^$', TemplateView.as_view(template_name='homes.html'), name='homes'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
 
   
  ]

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

