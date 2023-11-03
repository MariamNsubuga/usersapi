from django.urls import path
from .views import *
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
     path('contributor/register/', ContributorRegistration.as_view(), name='contributor-register'),
    path('admins/register/', AdminRegistration.as_view(), name='admin-register'),
    path('contributor/login/', ContributorLoginObtainToken.as_view(), name='contributor-login'),
    path('admins/login/', AdminLoginObtainToken.as_view(), name='admin-login'),
    # path('token/verify/', TokenVerify.as_view(), name='token-verify'),
    # path('token/refresh/', TokenRefresh.as_view(), name='token-refresh' # path('token/verify/', TokenVerify.as_view(), name='token-verify'),),jwt_views.TokenRefreshView.as_view()
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token-refresh'),
     path('token/verify/', jwt_views.TokenVerifyView.as_view(), name='token-verify'),
]

