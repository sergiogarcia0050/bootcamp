from rest_framework import routers
from events.views.events import EventsViewSet


router = routers.DefaultRouter()
router.register(r'events', EventsViewSet)

urlpatterns = router.urls
