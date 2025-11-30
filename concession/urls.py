from django.urls import path
from concession.views import ConcessionnaireListView, ConcessionnaireDetailView, VehiculeListView, VehiculeDetailView

urlpatterns = [
    path('concessionnaires/', ConcessionnaireListView.as_view(), name='concessionnaire-list'),
    path('concessionnaires/<int:pk>/', ConcessionnaireDetailView.as_view(), name='concessionnaire-detail'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/', VehiculeListView.as_view(), name='vehicule-list'),
    path('concessionnaires/<int:concessionnaire_id>/vehicules/<int:vehicule_id>/', VehiculeDetailView.as_view(), name='vehicule-detail'),
]
