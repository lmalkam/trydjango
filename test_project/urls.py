"""test_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path, include  #url
from blog.views import (blog_post_detail_view , blog_post_list_view , blog_post_create_view , blog_post_update_view , blog_post_delete_view)
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from .views import (home_page , contact_page , about_page ,  example_page , form_page)

from searches.views import (search_view)
urlpatterns = [
    path('',home_page),
    path('search/', search_view),
    # path('blog/',blog_post_list_view),
    path('blog-new/',blog_post_create_view),
    path('blog/', include('blog.urls')),
    # path('blog-new/',blog_post_create_view),
    # path('blog/<str:slug>/', blog_post_detail_view),
    # path('blog/<str:slug>/edit/', blog_post_update_view),
    # path('blog/<str:slug>/delete/', blog_post_delete_view),
    re_path(r'^about?/$',about_page),
    path('contact/',contact_page),
    path('admin/', admin.site.urls),
    path('example/', example_page),
    path('form/' , form_page),

    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),  
]
