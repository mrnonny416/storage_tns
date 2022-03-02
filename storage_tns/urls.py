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
from storage_tns_app.views import delete_material,delete_equipment,login,select,show_material,show_equipment,addlist,edit_equipment,edit_equipment_detail,edit_material,edit_material_detail,test,edit_equipment_save,edit_material_save,main,add_storage
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',login,name='login'),
    url(r'^select$',select,name='select'),
    url(r'^show_material$',show_material,name='show_material'),
    url(r'^show_equipment$',show_equipment,name='show_equipment'),
    url(r'^addlist$',addlist,name='addlist'),
    url(r'^edit_equipment$',edit_equipment,name='edit_equipment'),
    url(r'^edit_equipment_detail$',edit_equipment_detail,name='edit_equipment_detail'),
    url(r'^edit_material$',edit_material,name='edit_material'),
    url(r'^edit_material_detail$',edit_material_detail,name='edit_material_detail'),
    url(r'^edit_equipment_save$',edit_equipment_save,name='edit_equipment_save'),
    url(r'^edit_material_save$',edit_material_save,name='edit_material_save'),
    url(r'^delete_material$',delete_material,name='delete_material'),
    url(r'^delete_equipment$',delete_equipment,name='delete_equipment'),
    url(r'^test$',test,name='test'),
    url(r'^main$',main,name='main'),
    url(r'^add_storage$',add_storage,name='add_storage'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL ,document_root=settings.MEDIA_ROOT)