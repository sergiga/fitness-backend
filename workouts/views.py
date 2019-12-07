from rest_framework import viewsets
from workouts.models import Workout
from workouts.serializers import WorkoutSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer
