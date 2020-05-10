"""Blog URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from blog_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.post_listView),
    url(r'^tag/(?P<tag_slug>[-\w]+)/$',views.post_listView,name="posts_by_tag"),
    url(r'^(?P<year>\d{4})/(?P<month>\d+)/(?P<day>\d{2})/(?P<slug_post>[-\w]+)/$',views.detailed_view,name="detail"),
    url(r'^(?P<id>\d+)/share/$',views.EmailSending_View)
]
