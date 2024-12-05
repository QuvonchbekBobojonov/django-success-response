from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from ..response import SuccessResponse


# Custom class for obtaining JWT access and refresh tokens, wrapping the response in SuccessResponse
class SuccessTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        # Call the original post method from TokenObtainPairView to handle token generation
        response = super().post(request, *args, **kwargs)
        # Return the token data in the custom SuccessResponse format
        return SuccessResponse(response.data)


# Custom class for refreshing JWT access tokens, wrapping the response in SuccessResponse
class SuccessTokenRefreshView(TokenRefreshView):
    def post(self, request, *args, **kwargs):
        # Call the original post method from TokenRefreshView to handle token refresh
        response = super().post(request, *args, **kwargs)
        # Return the refreshed token data in the custom SuccessResponse format
        return SuccessResponse(response.data)


# Custom class for verifying JWT tokens, wrapping the response in SuccessResponse
class SuccessTokenVerifyView(TokenVerifyView):
    def post(self, request, *args, **kwargs):
        # Call the original post method from TokenVerifyView to verify the token
        response = super().post(request, *args, **kwargs)
        # Return the verification result in the custom SuccessResponse format
        return SuccessResponse(response.data)
