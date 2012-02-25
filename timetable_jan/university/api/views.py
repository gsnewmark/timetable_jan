from djangorestframework.views import ModelView
from djangorestframework.mixins import ReadModelMixin


class InstanceReadOnlyModelView(ReadModelMixin, ModelView):
    """
    A view which provides default read access to a model instance.
    """
    _suffix = 'InstanceReadOnly'