from rest_framework import viewsets
from .mixins import (
    SuccessCreateModelMixin,
    SuccessListModelMixin,
    SuccessRetrieveModelMixin,
    SuccessUpdateModelMixin,
    SuccessDestroyModelMixin,
)


# ViewSet for read-only operations (list and retrieve) with standardized success responses.
class SuccessReadOnlyModelViewSet(SuccessListModelMixin, SuccessRetrieveModelMixin, viewsets.GenericViewSet):
    """
    A ViewSet that provides read-only actions (list and retrieve) for a model.
    """
    # Restrict HTTP methods to only read operations.
    http_method_names = ['get', 'head', 'options']


# ViewSet for full CRUD operations with standardized success responses.
class SuccessModelViewSet(
    SuccessListModelMixin,
    SuccessCreateModelMixin,
    SuccessRetrieveModelMixin,
    SuccessUpdateModelMixin,
    SuccessDestroyModelMixin,
    viewsets.ModelViewSet  # Provides full Model CRUD capabilities.
):
    """
    A ViewSet that provides full CRUD operations for a model with standardized success responses.
    """
    # Allow only standard CRUD methods.
    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options']
