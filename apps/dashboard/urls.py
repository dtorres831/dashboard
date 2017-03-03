from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='my_home' ),
    url(r'^admin/$', views.admin, name='my_admin_home'),
    url(r'^admin/users/edit/(?P<id>\d+)$', views.edit, name='my_edit'),
    url(r'^admin/updateinfo/(?P<id>\d+)$', views.updateinfo, name='my_info_update'),
    url(r'^admin/updatepassword/(?P<id>\d+)$', views.updatepass, name='my_pass_update'),
    url(r'^profile/(?P<id>\d+)$', views.profile, name='my_profile'),
    url(r'^profile/messages/(?P<id>\d+)$', views.createmessage, name='create_message'),
    url(r'^profile/post/(?P<id>\d+)$', views.createpost, name='create_post'),
    url(r'^users/edit/(?P<id>\d+)$', views.useredit, name='my_user_edit'),
    url(r'^users/updatedescription/(?P<id>\d+)$', views.userdes, name='description_update'),
    url(r'^logout/$', views.logout, name='my_logout'),
]
