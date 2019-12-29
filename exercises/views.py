from rest_framework import viewsets
from exercises.models import Exercise, Muscle
from exercises.serializers import ExerciseSerializer, MuscleSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
