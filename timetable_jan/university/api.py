from django.conf.urls.defaults import patterns, include, url
from django.core.urlresolvers import reverse
from djangorestframework.resources import ModelResource
from djangorestframework.views import ListOrCreateModelView, InstanceModelView
from timetable_jan.university.models import *


#------------------------ Resources ----------------------------------
class UniversityResource(ModelResource):
    model = University


class BuildingResource(ModelResource):
    model = Building
    
    def university(self, instance):
        return reverse('university', kwargs={'id': instance.university.id})

class RoomResource(ModelResource):
    model = Room

    def building(self, instance):
        return reverse('building', kwargs={'id': instance.building.id, 'university': instance.building.university.id})
    
    
#------------------------ API links ----------------------------------
urls = patterns('',
    url(r'^$', ListOrCreateModelView.as_view(resource=UniversityResource), name='universities'),
    url(r'^(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=UniversityResource), name='university'),
    url(r'^(?P<university>[^/]+)/buildings/$', ListOrCreateModelView.as_view(resource=BuildingResource), name='buildings'),
    url(r'^(?P<university>[^/]+)/buildings/(?P<id>[^/]+)/$', InstanceModelView.as_view(resource=BuildingResource), name='building'),
    url(r'^[^/]+/buildings/(?P<building>[^/]+)/rooms/$', ListOrCreateModelView.as_view(resource=RoomResource), name='rooms'),
)
