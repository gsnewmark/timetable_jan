from django.conf.urls.defaults import patterns, url
from djangorestframework.views import ListModelView
from timetable_jan.university.api.views import InstanceReadOnlyModelView
from timetable_jan.university.api.resources import *


urlpatterns = patterns('',
    url(r'^universities/$',
        ListModelView.as_view(resource=UniversityResource),
        name='universities'),
    url(r'^universities/(?P<id>[^/]+)/$',
        InstanceReadOnlyModelView.as_view(resource=UniversityResource),
        name='university'),
    url(r'^universities/(?P<id>[^/]+)/terms/$',
        ListModelView.as_view(resource=AcademicTermResource),
        name='terms'),
    url(r'^universities/(?P<id>[^/]+)/terms/(?P<pk>[^/]+)/$',
        InstanceReadOnlyModelView.as_view(resource=UniversityResource),
        name='term'),
)