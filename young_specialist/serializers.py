from rest_framework import serializers
from .models import Organization, SystemUser, YoungSpecialistIndicators, MonthlyFormHeader, MonthlyFormLine

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class SystemUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemUser
        fields = '__all__'

class YoungSpecialistIndicatorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoungSpecialistIndicators
        fields = '__all__'

class MonthlyFormHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyFormHeader
        fields = '__all__'

class MonthlyFormLineSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonthlyFormLine
        fields = '__all__'