from django.urls import path
from . import views

urlpatterns = [

    path('academics/', views.academics_view, name='academics'),
    path('upload-document/', views.document_upload_view, name='upload_document'),
    path('application-status/', views.application_status_view, name='application_status'),

]
