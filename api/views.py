# we import our some staffs below here.
from rest_framework import viewsets
from .serializers import AfricanLeadersSerializer
from .models import AfricanLeaders

# we create our views here.
class AfricanLeadersViewset(viewsets.ModelViewSet):
    queryset=AfricanLeaders.objects.all()
    serializer_class=AfricanLeadersSerializer
    # we can add permission classes here if needed  

 



