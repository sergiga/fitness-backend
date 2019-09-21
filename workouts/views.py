from rest_framework import viewsets
from workouts.models import (
    Workout, Round, RoundSet, Exercise, Muscle,
)
from workouts.serializers import (
    WorkoutSerializer, RoundSerializer, RoundSetSerializer,
    ExerciseSerializer, MuscleSerializer,
)

class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class RoundViewSet(viewsets.ModelViewSet):
    queryset = Round.objects.all()
    serializer_class = RoundSerializer


class RoundSetViewSet(viewsets.ModelViewSet):
    queryset = RoundSet.objects.all()
    serializer_class = RoundSetSerializer


class ExerciseViewSet(viewsets.ModelViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class MuscleViewSet(viewsets.ModelViewSet):
    queryset = Muscle.objects.all()
    serializer_class = MuscleSerializer
