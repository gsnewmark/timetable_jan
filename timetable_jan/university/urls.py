from django.conf.urls.defaults import patterns, include, url
from timetable_jan.university.ajax_views import *
from django.views.generic import TemplateView

urlpatterns = patterns('',
    (r'^$', 'timetable_jan.university.views.index'),
    (r'^help/$', 'timetable_jan.university.views.help'),
    (r'^about/$', 'timetable_jan.university.views.about'),
    (r'^contacts/$', 'timetable_jan.university.views.contacts'),
    (r'^choose-subjects/(?P<timetable_id>\d+)/$', 'timetable_jan.university.views.choose_subjects'),
    url(r'^render/(?P<encoded_groups>[\d/]+)/$', 'timetable_jan.university.views.timetable', {'action': 'render'}, name='render'),
    url(r'^ical/(?P<encoded_groups>[\d/]+)/$', 'timetable_jan.university.views.timetable', {'action': 'ical'}, name='ical'),
    (r'^rooms-status/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'timetable_jan.university.views.rooms_status'),
    (r'^lecturer-timetable/$', 'timetable_jan.university.views.lecturer_timetable'),
    (r'^robots.txt$', 'timetable_jan.university.views.robots_txt'),
    (r'autocomplete/room/$', RoomAutocompleteView.as_view()),
    (r'autocomplete/lecturer/$', LecturerAutocompleteView.as_view()),
    (r'autocomplete/discipline/$', DisciplineAutocompleteView.as_view()),
    (r'autocomplete/extra-courses/$', ExtraCoursesAutocompleteView.as_view()),
    (r'autocomplete/test/$', TemplateView.as_view(template_name='autocomplete_test.html')),
    (r'create-timetable/$', UnifiedTimetableProcessView.as_view(template_name='create_timetable.html')),
)
