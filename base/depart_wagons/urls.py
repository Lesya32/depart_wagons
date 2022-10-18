from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('tmp', views.tmp3),
    path('sending', views.sending, name='sending'),
    path('list_view', views.list_view.as_view(), name='list_view'),

]