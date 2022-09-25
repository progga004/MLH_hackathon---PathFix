from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('SearchPath', views.redirectCoursesToJobsView, name='redirectCoursesToJobsView')
]