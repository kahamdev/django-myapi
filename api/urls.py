# we import some staffs below here.
from rest_framework import routers
from .views import AfricanLeadersViewset
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

# we add routers below
router=routers.DefaultRouter()

# we register our viewset with the router
router.register('african-leaders',AfricanLeadersViewset,basename="african-leaders") # type: ignore

# we add path router urls below 
urlpatterns=[ # type: ignore
    path('/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'), # type: ignore
    path('/token/refresh',TokenRefreshView.as_view(),name='token_refresh'), # type: ignore
    path('',include(router.urls)) # type: ignore
] 



