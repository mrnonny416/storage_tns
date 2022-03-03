"""storage_tns URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from xml.dom.minidom import Document
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from storage_tns_app.views import login,test,main,add_storage,product,logout 
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login,name='login'),
    url(r'^test$',test,name='test'),
    url(r'^main$',main,name='main'),
    url(r'^add_storage$',add_storage,name='add_storage'),
    url(r'^product$',product,name='product'),
    url(r'^logout$',logout,name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)