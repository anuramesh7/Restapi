from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from restapp.views import RideStatusUpdateView, RideViewset
from restapp import views

router = routers.DefaultRouter()
router.register('rides',RideViewset)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('register/', views.CreateUserview.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('home/', views.home.as_view(), name='home'),
    path('rides/<int:pk>/update-status/', RideStatusUpdateView.as_view({'patch': 'update'})),
]
