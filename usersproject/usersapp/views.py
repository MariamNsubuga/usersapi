from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from .models import *
from .serializers import *
from rest_framework import permissions
from rest_framework import generics

class ContributorRegistration(generics.CreateAPIView):
    queryset = Contributor.objects.all()
    serializer_class = ContributorSerializer
    permission_classes = [permissions.AllowAny]

class AdminRegistration(generics.CreateAPIView):
    queryset = Admins.objects.all()
    serializer_class = AdminSerializer
    permission_classes = [permissions.AllowAny]

class ContributorLoginObtainToken(TokenObtainPairView):
    serializer_class = ContributorSerializer

class AdminLoginObtainToken(TokenObtainPairView):
    serializer_class = AdminSerializer

class TokenVerify(RefreshToken):
    pass

class TokenRefresh(RefreshToken):
    pass


class IsContributor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Check if the user is a Contributor or Admin
        return isinstance(request.user, Contributor) or request.user.is_staff

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return isinstance(request.user, Admins) or request.user.is_staff

# class CustomLoginView(TokenObtainPairView):
#     # serializer_class = CustomLoginSerializer

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)

#         if serializer.is_valid(raise_exception=True):
#             user_type = serializer.validated_data['user_type']
#             if user_type == 'contributor':
#                 return ContributorLoginObtainToken.as_view()(request._request)
#             elif user_type == 'admin':
#                 return AdminLoginObtainToken.as_view()(request._request)
#             else:
#                 return Response({'error': 'Invalid user type'}, status=400)