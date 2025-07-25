# we import some staffs below here.
from rest_framework import routers
from .views import AfricanLeadersViewset
from django.urls import path,include

# we add routers below
router=routers.DefaultRouter()

# we register our viewset with the router
router.register('african-leaders',AfricanLeadersViewset,basename="african-leaders") # type: ignore

# we add path router urls below 
urlpatterns=[
    path('',include(router.urls)) # type: ignore
] 



