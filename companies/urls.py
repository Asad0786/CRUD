from django.urls import include, path
from .apis import CustomCompanyViewSet, EmployeeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'new',CustomCompanyViewSet)
router.register(r'employees', EmployeeViewSet, basename='employee')


urlpatterns=[
    path("",include(router.urls)),
    
]