from rest_framework import routers
from workouts.views import WorkoutViewSet

router = routers.DefaultRouter()

router.register(r'workouts', WorkoutViewSet, base_name='workouts')

urlpatterns = router.urls
