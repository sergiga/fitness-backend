from django.db import models
from core.models import BaseModel
from core.utils import Level, RepUnit

class Workout(BaseModel):
    name = models.CharField(max_length=100)
    level = models.IntegerField(
        choices=Level.choices(),
        default=Level.INTERMEDIATE
    )

    def __str__(self):
        return self.name


class WorkoutSet(BaseModel):
    sets = models.IntegerField()
    order = models.IntegerField()

    workout = models.ForeignKey(
        'workouts.Workout',
        related_name='workout_sets',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} {}'.format(self.workout.name, self.order)


class ExerciseInSet(BaseModel):
    reps = models.IntegerField()
    rep_unit = models.IntegerField(
        choices=RepUnit.choices(),
        default=RepUnit.REPS
    )

    workout_set = models.ForeignKey(
        'workouts.WorkoutSet',
        related_name='exercises_in_set',
        on_delete=models.CASCADE
    )
    exercise = models.ForeignKey(
        'exercises.Exercise',
        related_name='exercises_in_set',
        on_delete=models.CASCADE
    )
    parent = models.OneToOneField(
        'self',
        related_name='child',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {}'.format(
            self.workout_set.__str__(),
            self.exercise.__str__()
        )

class Training(BaseModel):
    date = models.DateField()
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)

    workout = models.ForeignKey(
        'workouts.Workout',
        related_name='trainings',
        on_delete=models.CASCADE
    )
    exercise_in_set = models.ForeignKey(
        'workouts.ExerciseInSet',
        related_name='trainings',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {}'.format(
            self.workout.__str__(),
            self.date
        )

class TrainingExercise(BaseModel):
    reps = models.IntegerField()

    workout = models.ForeignKey(
        'workouts.Workout',
        related_name='training_exercises',
        on_delete=models.CASCADE
    )
    exercise_in_set = models.ForeignKey(
        'workouts.ExerciseInSet',
        related_name='training_exercises',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return '{} - {}'.format(
            self.workout.__str__(),
            self.exercise_in_set.__str__()
        )
