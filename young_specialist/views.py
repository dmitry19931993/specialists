from rest_framework import generics
from rest_framework.response import Response
from .models import Organization, SystemUser, YoungSpecialistIndicators, MonthlyFormHeader, MonthlyFormLine
from .serializers import OrganizationSerializer, SystemUserSerializer, YoungSpecialistIndicatorsSerializer, \
    MonthlyFormHeaderSerializer, MonthlyFormLineSerializer

from rest_framework.views import APIView
from .services import data_filter


class OrganizationListCreate(generics.ListCreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer


class SystemUserListCreate(generics.ListCreateAPIView):
    queryset = SystemUser.objects.all()
    serializer_class = SystemUserSerializer


class YoungSpecialistIndicatorsListCreate(generics.ListCreateAPIView):
    queryset = YoungSpecialistIndicators.objects.all()
    serializer_class = YoungSpecialistIndicatorsSerializer


class MonthlyFormHeaderListCreate(generics.ListCreateAPIView):
    queryset = MonthlyFormHeader.objects.all()
    serializer_class = MonthlyFormHeaderSerializer


class MonthlyFormLineListCreate(generics.ListCreateAPIView):
    queryset = MonthlyFormLine.objects.all()
    serializer_class = MonthlyFormLineSerializer


class DownloadReportAPIView(APIView):

    def get(self, request, *args, **kwargs):
        start_month = request.GET.get('start_month')
        end_month = request.GET.get('end_month')
        if not start_month or not end_month:
            return Response({'error': 'Both start_month and end_month are required.'}, status=400)

        return data_filter(start_month, end_month)
