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

from django.conf.urls import url
<<<<<<< Updated upstream
from storage_tns_app.views import index,login,select
from django.contrib import admin
=======
from storage_tns_app.views import index,admin,login,select,show_material

>>>>>>> Stashed changes


urlpatterns = [
    url('admin', admin.site.urls, name='admin'),
    url(r'^$',index,name='index'),
    url(r'^login$',login,name='login'),
    url(r'^select$',select,name='select'),
<<<<<<< Updated upstream
=======
    url(r'^$',show_material,name='show_material'),
>>>>>>> Stashed changes
]
