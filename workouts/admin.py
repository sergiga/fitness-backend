from django.contrib import admin
from workouts.models import (
    Workout, WorkoutSet, ExerciseInSet,
    Training, TrainingExercise
)

@admin.register(
    Workout, WorkoutSet, ExerciseInSet,
    Training, TrainingExercise
)
class WorkoutAdmin(admin.ModelAdmin):
    pass
