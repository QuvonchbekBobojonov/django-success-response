from rest_framework.mixins import (
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
)
from .response import SuccessResponse


# Mixin for creating objects with a standardized success response.
class SuccessCreateModelMixin(CreateModelMixin):
    """
    Custom mixin to wrap the response in SuccessResponse after creating a new object.
    """
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return SuccessResponse(response.data)


# Mixin for listing objects with a standardized success response.
class SuccessListModelMixin(ListModelMixin):
    """
    Custom mixin to wrap the response in SuccessResponse when listing objects.
    """
    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        return SuccessResponse(response.data)


# Mixin for retrieving objects with a standardized success response.
class SuccessRetrieveModelMixin(RetrieveModelMixin):
    """
    Custom mixin to wrap the response in SuccessResponse when retrieving an object.
    """
    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        return SuccessResponse(response.data)


# Mixin for updating objects with a standardized success response.
class SuccessUpdateModelMixin(UpdateModelMixin):
    """
    Custom mixin to wrap the response in SuccessResponse after updating an object.
    """
    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        return SuccessResponse(response.data)


# Mixin for deleting objects with a standardized success response.
class SuccessDestroyModelMixin(DestroyModelMixin):
    """
    Custom mixin to wrap the response in SuccessResponse after deleting an object.
    """
    def destroy(self, request, *args, **kwargs):
        # Call the default destroy method to handle deletion logic.
        super().destroy(request, *args, **kwargs)
        # Return a standardized success response with a deletion confirmation message.
        return SuccessResponse({'detail': 'Deleted'})
