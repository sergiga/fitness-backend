from rest_framework import serializers
from workouts.models import (
    Workout, Round, RoundSet, Exercise, Muscle
)


class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = ['id', 'name', 'rounds']


class RoundSerializer(serializers.ModelSerializer):
    class Meta:
        model = Round
        fields = ['id', 'name', 'order', 'workout', 'sets', 'exercises']


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ['id', 'name', 'sets', 'rounds', 'muscles']


class RoundSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoundSet
        fields = ['id', 'order', 'repetitions', 'seconds', 'wourkout_round', 'exercise']


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = ['id', 'name']
