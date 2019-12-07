from rest_framework import routers
from workouts.views import (
    WorkoutViewSet, RoundViewSet, RoundSetViewSet,
    ExerciseViewSet, MuscleViewSet
)

router = routers.DefaultRouter()

router.register(r'workouts', WorkoutViewSet, base_name='words')
router.register(r'rounds', RoundViewSet, base_name='rounds')
router.register(r'round_sets', RoundSetViewSet, base_name='round_sets')
router.register(r'exercises', ExerciseViewSet, base_name='exercises')
router.register(r'muscles', MuscleViewSet, base_name='muscles')

urlpatterns = router.urls
