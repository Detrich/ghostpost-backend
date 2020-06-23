from ghostpostapi.views import postsViewSet

from rest_framework.routers import DefaultRouter

from django.conf.urls import include, url

router = DefaultRouter()

router.register(r'posts', postsViewSet,basename='RandB')


urlpatterns = [
    url(r'^api/',include(router.urls)),
]