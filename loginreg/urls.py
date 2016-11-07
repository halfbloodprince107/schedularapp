from django.conf.urls import url, include
from loginreg import views
from rest_framework.routers import DefaultRouter
from django.contrib.auth.decorators import login_required

router = DefaultRouter()
# router.register(r'login', views.Login)
router.register(r'register', views.Register)
router.register(r'role', views.Role)
# router.register(r'emails', views.ByEmailId, base_name='email')

urlpatterns = [

    url(r'^', include(router.urls)),

]
