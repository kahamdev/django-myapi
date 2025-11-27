# we import serializers from rest framework
from rest_framework import serializers

# we import AfricanLeaders model from django model
from .models import AfricanLeaders


class AfricanLeadersSerializer(serializers.ModelSerializer):
    class Meta:
        model = AfricanLeaders
        fields = "__all__"
