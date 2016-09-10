from django.conf.urls import url,include
from myapp import views

urlpatterns=[
url(r'^index/$',views.index,name="myappIndex"),
url(r'^formsubmit/$',views.formsubmission,name="form submit")
]
