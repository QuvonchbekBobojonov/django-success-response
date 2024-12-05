from rest_framework.generics import GenericAPIView
from .mixins import (
    SuccessCreateModelMixin,
    SuccessListModelMixin,
    SuccessRetrieveModelMixin,
    SuccessUpdateModelMixin,
    SuccessDestroyModelMixin,
)


# Custom API view for creating objects. Inherits from SuccessCreateModelMixin.
class SuccessCreateAPIView(SuccessCreateModelMixin, GenericAPIView):
    """
    Handles creating a new object via POST request.
    """
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Custom API view for listing objects. Inherits from SuccessListModelMixin.
class SuccessListAPIView(SuccessListModelMixin, GenericAPIView):
    """
    Handles listing objects via GET request.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# Custom API view for retrieving a single object. Inherits from SuccessRetrieveModelMixin.
class SuccessRetrieveAPIView(SuccessRetrieveModelMixin, GenericAPIView):
    """
    Handles retrieving a single object via GET request.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


# Custom API view for updating objects. Inherits from SuccessUpdateModelMixin.
class SuccessUpdateAPIView(SuccessUpdateModelMixin, GenericAPIView):
    """
    Handles updating an object via PUT or PATCH request.
    """
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# Custom API view for deleting objects. Inherits from SuccessDestroyModelMixin.
class SuccessDestroyAPIView(SuccessDestroyModelMixin, GenericAPIView):
    """
    Handles deleting an object via DELETE request.
    """
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Combined List and Create API view. Handles both GET (list) and POST (create).
class SuccessListCreateAPIView(SuccessCreateModelMixin, SuccessListModelMixin, GenericAPIView):
    """
    Handles listing objects via GET and creating new objects via POST request.
    """
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


# Combined Retrieve and Update API view. Handles both GET (retrieve) and PUT/PATCH (update).
class SuccessRetrieveUpdateAPIView(SuccessRetrieveModelMixin, SuccessUpdateModelMixin, GenericAPIView):
    """
    Handles retrieving an object via GET and updating it via PUT or PATCH request.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


# Combined Retrieve and Destroy API view. Handles both GET (retrieve) and DELETE (destroy).
class SuccessRetrieveDestroyAPIView(SuccessRetrieveModelMixin, SuccessDestroyModelMixin, GenericAPIView):
    """
    Handles retrieving an object via GET and deleting it via DELETE request.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Combined Retrieve, Update, and Destroy API view.
class SuccessRetrieveUpdateDestroyAPIView(
    SuccessRetrieveModelMixin,
    SuccessUpdateModelMixin,
    SuccessDestroyModelMixin,
    GenericAPIView
):
    """
    Handles retrieving, updating, and deleting an object via GET, PUT/PATCH, or DELETE request.
    """
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
