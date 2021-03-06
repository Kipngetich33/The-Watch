from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.landing,name = 'landingUrl'),
    url(r'^profile/create',views.create_profile,name = 'create_profileUrl'),
    url(r'^post/create',views.post,name = 'postUrl'),
    url(r'^business/create',views.business,name = 'businessUrl'),
    url(r'^business/view',views.view_business,name = 'viewBusinessUrl'),
    url(r'^move/out',views.move_out,name = 'move_outUrl'),
    url(r'^moving/out/(\d+)',views.moving,name = 'movingUrl'),
]