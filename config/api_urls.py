from rest_framework import routers

from mhu_ped_oauth_provider.users.api.viewsets import UserViewSet, GroupViewSet

app_name = "apis"
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, base_name='user')
router.register(r'groups', GroupViewSet, base_name='group')

urlpatterns = router.urls
