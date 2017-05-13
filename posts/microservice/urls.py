from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import SimpleRouter

from microservice.views import PostViewSet


router = SimpleRouter()

router.register(u'1.0/posts', PostViewSet)

urlpatterns = router.urls + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)