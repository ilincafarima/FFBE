from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', landing_page, name='landing_page'),
    path('register/', register, name='register'),  
    path('login/', login_view, name='login'),
    path('search/', search_view, name='search'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)