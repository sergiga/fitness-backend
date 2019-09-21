from django.contrib import admin
from workouts.models import (
    Workout, Round, RoundSet, Exercise, Muscle
)

@admin.register(Workout, Round, RoundSet, Exercise, Muscle)
class AuthorAdmin(admin.ModelAdmin):
    pass
