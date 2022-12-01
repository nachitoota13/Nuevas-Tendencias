from django.urls import path
from TiendaDepot import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="Index"),
    path('\popu', views.indexPopu, name="IndexPopu"),
    path('\promo', views.indexPromo, name="IndexPromo"),
]
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)