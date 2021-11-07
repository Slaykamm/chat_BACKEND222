"""chat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
#from rest_framework.urlpatterns import format_suffix_patterns
from message import views
from message.views import RoomApiDeleteView
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'roomsAPI', views.GroupViewSet)
router.register(r'messageAPI', views.MessageViewSet)
router.register(r'userAPI', views.AuthorViewSet)
router.register(r'loginAPI', views.LoginViewSet)
router.register(r'roomsAPI/roomdelete/<int:pk>', RoomApiDeleteView)
router.register(r'roomsAPI/<int:pk>/', views.GroupViewUpdate)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('message.urls')),
    path('accounts/', include('allauth.urls')),
    path('sign/', include('sign.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]


# включаем возможность обработки картинок
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)