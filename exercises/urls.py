from rest_framework import routers
from exercises.views import ExerciseViewSet

router = routers.DefaultRouter()

router.register(r'exercises', ExerciseViewSet, base_name='exercises')

urlpatterns = router.urls