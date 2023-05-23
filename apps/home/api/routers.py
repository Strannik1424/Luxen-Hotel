from django.urls import path, include
from rest_framework import routers

from apps.apartment.views import ApartmentViewSets
from apps.hoteInfo.views import HotelInfoViewSets, SidebarViewSets, TeamViewSets
from apps.contact.views import ContactViewSets, ContactFormViewSets
from apps.home.views import BookNowViewSet

router = routers.SimpleRouter()
router.register(r'BookNows', BookNowViewSet)

router.register(r'apartment', ApartmentViewSets)
router.register(r'hotelInfo', HotelInfoViewSets)
router.register(r'contact', ContactViewSets)
router.register(r'messageUsers', ContactFormViewSets)
router.register(r'sidebar', SidebarViewSets)
router.register(r'team', TeamViewSets)


urlpatterns = [
    path('api/v1/', include(router.urls)),
]



