# we import our some staffs below here.
from rest_framework import viewsets
#from rest_framework.authentication import TokenAuthentication
from .models import AfricanLeaders

# we create our views here.
class AfricanLeadersViewset(viewsets.ModelViewSet):
    queryset=AfricanLeaders.objects.all()
    serializer_class=AfricanLeaders
    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]
 



