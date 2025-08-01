"""
URL configuration for myproject project.
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView


urlpatterns = [# type: ignore
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api/auth/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'), # type: ignore
    path('api/auth/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'), # type: ignore
]
