from rest_framework import serializers
from workouts.models import Workout, WorkoutSet, ExerciseInSet


class ExerciseInSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseInSet
        fields = [
            'id',
            'reps',
            'rep_unit',
            'workout_set',
            'group',
            'group_order',
        ]
        extra_kwargs = {
            'workout_set': {'required': False},
        }


class WorkoutSetSerializer(serializers.ModelSerializer):
    exercises_in_set = ExerciseInSetSerializer(many=True)

    class Meta:
        model = WorkoutSet
        fields = [
            'id',
            'sets',
            'order',
            'workout',
            'exercises_in_set'
        ]
        extra_kwargs = {
            'workout': {'required': False}
        }

    def create(self, validated_data):
        exercises_data = validated_data.pop('exercises_in_set')
        instance = WorkoutSet.objects.create(**validated_data)

        # Exercises in set

        for exercise_data in exercises_data:
            exercise_data['workout_set'] = instance.id
        serializer = ExerciseInSetSerializer(data=exercises_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return instance


class WorkoutSerializer(serializers.ModelSerializer):
    workout_sets = WorkoutSetSerializer(many=True)

    class Meta:
        model = Workout
        fields = ['id', 'name', 'level', 'workout_sets']

    def create(self, validated_data):
        workout_sets_data = validated_data.pop('workout_sets')
        instance = Workout.objects.create(**validated_data)

        # Workout sets

        for workout_set_data in workout_sets_data:
            workout_set_data['workout'] = instance.id
        serializer = WorkoutSetSerializer(data=workout_sets_data, many=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return instance
