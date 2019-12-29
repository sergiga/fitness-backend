from rest_framework import routers
from exercises.views import ExerciseViewSet, MuscleViewSet

router = routers.DefaultRouter()

router.register(r'exercises', ExerciseViewSet, base_name='exercises')
router.register(r'muscles', MuscleViewSet, base_name='muscles')

urlpatterns = router.urls