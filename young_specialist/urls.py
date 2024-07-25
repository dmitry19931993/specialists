from django.urls import path
from django.views.generic import TemplateView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('organizations/', views.OrganizationListCreate.as_view(), name='organization-list-create'),
    path('system-users/', views.SystemUserListCreate.as_view(), name='systemuser-list-create'),
    path('young-specialist-indicators/', views.YoungSpecialistIndicatorsListCreate.as_view(), name='young-specialist-indicators-list-create'),
    path('monthly-form-headers/', views.MonthlyFormHeaderListCreate.as_view(), name='monthly-form-header-list-create'),
    path('monthly-form-lines/', views.MonthlyFormLineListCreate.as_view(), name='monthly-form-line-list-create'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('download-report/', views.DownloadReportAPIView.as_view(), name='download-report'),
    path('report/', TemplateView.as_view(template_name='report.html'), name='report'),
]