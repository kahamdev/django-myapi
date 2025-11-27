# we import our some staffs below here.
from rest_framework import viewsets
from .serializers import AfricanLeadersSerializer
from .models import AfricanLeaders
from rest_framework.permissions import IsAuthenticated


# we create our views here.
class AfricanLeadersViewset(viewsets.ModelViewSet):
    queryset = AfricanLeaders.objects.all()
    serializer_class = AfricanLeadersSerializer
    permission_classes = [IsAuthenticated]
