from django.conf.urls import url,include
from myapp import views

urlpatterns=[
url(r'^index/$',views.index,name="myappIndex"),
url(r'^formsubmit/$',views.dummy,name="form submit"),
url(r'^login/',views.studlogin),
url(r'^details/(?P<pk>\d+)/$',views.details,name="detail page"),
url(r'^dummy/$',views.dummy,name="post_new")
]
