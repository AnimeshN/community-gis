from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer

from .models import CovidHospbeds


class CovidHospbedserializer(GeoFeatureModelSerializer):
    class Meta:
        model = CovidHospbeds
        geo_field = "geom"
        fields = "__all__"
