from rest_framework import viewsets, permissions

from .serializers import CohortSerializer, StudentSerializer
from .models import Cohort, Student


class CohortViewSet(viewsets.ModelViewSet):
    queryset = Cohort.objects.all()
    serializer_class = CohortSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
