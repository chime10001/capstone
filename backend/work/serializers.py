from .models import workTable
from rest_framework import serializers


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = workTable
        fields = '__all__'
    