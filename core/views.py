from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Patient, Doctor, PatientDoctorMapping
from .serializers import (
    PatientSerializer,
    DoctorSerializer,
    PatientDoctorMappingSerializer
)


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Only show patients created by logged-in user
        return Patient.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign logged-in user
        serializer.save(user=self.request.user)


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    permission_classes = [IsAuthenticated]


class PatientDoctorMappingViewSet(viewsets.ModelViewSet):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]