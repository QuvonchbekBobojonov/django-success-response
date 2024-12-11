from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView, TokenViewBase
from rest_framework.exceptions import ValidationError
from rest_framework.request import Request
from ..response import SuccessResponse


class SuccessTokenViewBase(TokenViewBase):
    """Base class for customizing JWT token-related views with SuccessResponse."""

    def handle_exception(self, serializer, request_data):
        """Handle exceptions during token processing and return a proper SuccessResponse."""
        try:
            serializer.is_valid(raise_exception=True)
        except ValidationError as e:
            detail = ' '.join(
                f"{field}: {' '.join(errors)}" for field, errors in e.detail.items()
            )
            return SuccessResponse({'detail': detail}, success=False)
        except Exception as e:
            return SuccessResponse({'detail': str(e)}, success=False)

        return SuccessResponse(serializer.data)

    def post(self, request: Request, *args, **kwargs):
        """Process POST requests using the appropriate serializer."""
        serializer = self.get_serializer(data=request.data)
        return self.handle_exception(serializer, request.data)


# Custom class for obtaining JWT access and refresh tokens
class SuccessTokenObtainPairView(SuccessTokenViewBase, TokenObtainPairView):
    """Override TokenObtainPairView to wrap the response in SuccessResponse."""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return SuccessResponse(response.data)


# Custom class for refreshing JWT access tokens
class SuccessTokenRefreshView(SuccessTokenViewBase, TokenRefreshView):
    """Override TokenRefreshView to wrap the response in SuccessResponse."""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return SuccessResponse(response.data)


# Custom class for verifying JWT tokens
class SuccessTokenVerifyView(SuccessTokenViewBase, TokenVerifyView):
    """Override TokenVerifyView to wrap the response in SuccessResponse."""

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return SuccessResponse(response.data)
