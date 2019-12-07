from django.db import models
from core.models import BaseModel
from core.utils import Level


class Exercise(BaseModel):
    name = models.CharField(max_length=100)
    level = models.IntegerField(
        choices=Level.choices(),
        default=Level.INTERMEDIATE
    )

    def __str__(self):
        return self.name


class Muscle(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Equipment(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class MuscleInExercise(BaseModel):
    exercise = models.ForeignKey(
        'exercises.Exercise',
        related_name='muscles_in_exercise',
        on_delete=models.CASCADE
    )
    muscle = models.ForeignKey(
        'exercises.Muscle',
        related_name='muscles_in_exercise',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {}'.format(
            self.exercise.__str__(),
            self.muscle.__str__()
        )


class EquipmentInExercise(BaseModel):
    exercise = models.ForeignKey(
        'exercises.Exercise',
        related_name='muscles_in_exercise',
        on_delete=models.CASCADE
    )
    equipment = models.ForeignKey(
        'exercises.Equipment',
        related_name='equipments_in_exercise',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {}'.format(
            self.exercise.__str__(),
            self.equipment.__str__()
        )
