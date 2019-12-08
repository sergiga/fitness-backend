from django.contrib import admin
from exercises.models import (
    Exercise, Equipment, Muscle,
    EquipmentInExercise, MuscleInExercise
)

@admin.register(
    Exercise, Equipment, Muscle,
    EquipmentInExercise, MuscleInExercise
)
class WorkoutAdmin(admin.ModelAdmin):
    pass
