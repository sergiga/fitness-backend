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
        data['muscles'] = [m.id for m in Muscle.objects.filter(muscles_in_exercise__exercise=value)]
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
