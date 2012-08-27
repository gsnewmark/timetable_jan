#-*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from timetable.university.cb_views import *
from django.views.generic import TemplateView, RedirectView
from timetable.university.ajax_views import ajax_urls, UnifiedTimetableProcessView
from timetable.university.views import ICALView, TimetableView, TimetableMainView
from timetable.university.planning_views import PlanningLightView, PlanningLightRoomView, PlanningLightRoomDeleteView, PlanningAjaxView, PlanningRoomAddLessonsAjaxView, PlanningRoomDeleteLessonsAjaxView, PlanningRoomAjaxLecturerView, PlanningAddLessonsAjaxView, PlanningDeleteLessonsAjaxView


urlpatterns = patterns('',
    (r'^$', 'timetable.university.views.index'),
    (r'^help/$', 'timetable.university.views.help'),
    (r'^about/$', 'timetable.university.views.about'),
    (r'^contacts/$', 'timetable.university.views.contacts'),
    (r'^course-stats/$', 'timetable.university.planning_views.course_stats'),
    (r'^planning/$',
     'timetable.university.planning_views.choose_term_for_planning'),
    url(r'^planning-light/$',
        RedirectView.as_view(url='/planning/', permanent=False)),
    (r'^planning/(?P<term>\d+)/$',
     'timetable.university.planning_views.planning'),
    url(r'^planning-light/(?P<term>\d+)/$',
        PlanningLightView.as_view(), name='planning-light'),
    url(r'^planning/(?P<term>\d+)/add/lessons/$',
        PlanningAddLessonsAjaxView.as_view(), name='planning-add-lessons'),
    url(r'^planning/(?P<term>\d+)/delete/lessons/$',
        PlanningDeleteLessonsAjaxView.as_view(), name='planning-delete-lessons'),
    url(r'^planning-light/(?P<term>\d+)/(?P<room_id>\d+)/ajax/$',
        PlanningAjaxView.as_view(), name='planning-ajax'),
    url(r'^planning-light/(?P<term>\d+)/add/$',
        PlanningLightRoomView.as_view(), name='planning-light-room'),
    url(r'^planning-light/(?P<term>\d+)/delete/$',
        PlanningLightRoomDeleteView.as_view(), name='planning-light-room-delete'),
    url('^planning-light/(?P<term>\d+)/room/(?P<room_id>\d+)/add/ajax/$',
        PlanningRoomAddLessonsAjaxView.as_view(), name='planning-room-ajax'),
    url('^planning-light/(?P<term>\d+)/room/(?P<room_id>\d+)/delete/ajax/$',
        PlanningRoomDeleteLessonsAjaxView.as_view(), name='planning-room-ajax'),
    url('^planning-light/(?P<term>\d+)/lecturer/(?P<group_id>\d+)/ajax/$',
        PlanningRoomAjaxLecturerView.as_view(), name='planning-room-ajax-lecturer'),
    (r'^choose-subjects/(?P<timetable_id>\d+)/$',
     'timetable.university.views.choose_subjects'),
    url(r'^render/(?P<encoded_groups>[\d/]+)/$',
        TimetableMainView.as_view(), name='render-main'),
    url(r'^render/(?P<encoded_groups>[\d/]+)/group/(?P<group_to_show>\d+)/$',
        TimetableMainView.as_view(), name='render-main-group'),
    url(r'^render/(?P<encoded_groups>[\d/]+)/weeks/$',
        TimetableView.as_view(), name='render-all'),
    url(r'^render/(?P<encoded_groups>[\d/]+)/weeks/group/(?P<group_to_show>\d+)/$',
        TimetableView.as_view(), name='render-all-group'),
    url(r'^render/(?P<encoded_groups>[\d/]+)/week/(?P<week_to_show>\d+)/$',
        TimetableView.as_view(), name='render-week'),
    url(r'^render/(?P<encoded_groups>[\d/]+)/week/(?P<week_to_show>\d+)/group/(?P<group_to_show>\d+)/$',
        TimetableView.as_view(), name='render-week-group'),
    url(r'^ical/(?P<encoded_groups>[\d/]+)/$',
        ICALView.as_view(), name='ical'),
    (r'^rooms-status/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$',
     'timetable.university.views.rooms_status'),
    (r'^lecturer-timetable/$',
     'timetable.university.views.lecturer_timetable'),
    (r'^robots.txt$', 'timetable.university.views.robots_txt'),
    (r'^[a-z0-9]+.ics$', 'timetable.university.views.http_gone'),
    (r'^accounts/profile/$', 'timetable.university.views.profile'),
    url(r'^lesson/(?P<pk>\d+)/$',
        LessonDetailView.as_view(template_name="lesson.html"), name='lesson'),
    url(r'^course/create/$',
        CourseCreateView.as_view(template_name="course.html"), name='course'),
    (r'^autocomplete/', include(ajax_urls)),
    (r'create-timetable/$',
     UnifiedTimetableProcessView.as_view(
         template_name='create_timetable.html')),
    url(r'^feedback/$', FeedbackView.as_view(template_name='feedback.html')),
)
