from rest_framework import routers
from .views import UserCreateViewSet

router = routers.DefaultRouter()
router.register('createuser', UserCreateViewSet)
urlpatterns = router.urls 