from djangorestframework.resources import ModelResource
from timetable_jan.university.models import University, AcademicTerm
from django.core.urlresolvers import reverse


class UniversityResource(ModelResource):
    """
    An University has a name and a abbreviation.
    """
    model = University
    fields = ('id', 'name', 'abbr')


class AcademicTermResource(ModelResource):
    """
    An AcademicTerm has a university (foreign key), year, kind, season
    number of weeks, possibly a 'free' week, start date and exams
    start/end date.
    """
    model = AcademicTerm
    fields = ('university', 'pk', 'year', 'kind', 'season',
              'number_of_weeks', 'tcp_week', 'start_date',
              'exams_start_date', 'exams_end_date')

    def university(self, instance):
        return reverse('university', kwargs={'id': instance.university.id})
