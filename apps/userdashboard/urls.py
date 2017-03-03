from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_home' ),
    url(r'^signin$', views.signin, name='my_signin' ),
    url(r'^signin/verify$', views.vsignin, name='my_vsignin'),
    url(r'^register$', views.register, name='my_register'),
    url(r'^register/verify$', views.vregister, name='my_vregister')
]
