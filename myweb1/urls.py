
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *

#http://127.0.0.1:8000/detail/35/
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',index),
    url(r'^detail/(\d+)/$',detail,name='contact'),
    url(r'^delete/(\d+)/$',del_record,name='delete'),
    url(r'^edit/(\d+)/$',edit_record),
    url(r'^search_query/$',search),
    url(r'^contact/$',contact),
    url(r'^success/$',success),
    
]
