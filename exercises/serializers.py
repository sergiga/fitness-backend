from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from exercises.models import Exercise, MuscleInExercise, Muscle


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = [
            'id',
            'name',
            'level',
        ]

    def to_representation(self, value):
        data = super(ExerciseSerializer, self).to_representation(value)
        data['muscles_in_exercise'] = [
            {
                'id': muscle_in_exercise.id,
                'muscle_id': muscle_in_exercise.muscle_id,
                'exercise_id': muscle_in_exercise.exercise_id
            }
            for muscle_in_exercise in value.muscles_in_exercise.all().select_related('muscle')
        ]
        return data

    def to_internal_value(self, data):
        muscles = []
        for muscle_id in data.pop('muscles', []):
            muscle = Muscle.objects.filter(pk=muscle_id).first()
            if muscle:
                muscles.append(muscle)
            else:
                raise ValidationError(
                    detail=_('Muscle with id %s doesn`t exists' % (muscle_id))
                )
        data['muscles'] = muscles
        return data
    
    def create(self, validated_data):
        muscles = validated_data.pop('muscles')
        instance = Exercise.objects.create(**validated_data)

        for muscle in muscles:
            MuscleInExercise.objects.create(
                exercise=instance,
                muscle=muscle
            )
        return instance


class MuscleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Muscle
        fields = [
            'id',
            'name'
        ]
