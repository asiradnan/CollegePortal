from django.contrib import admin
from django.urls import path,include
from . import views 
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('accounts/', include('allauth.urls')),
    path('academics/',include('Academics.urls')),
    path('clubs/',include('Club.urls')),
    path('notice/',include('Notice.urls')),
    path('PostsNQueries/',include('PostsNQueries.urls')),
    path('about/',views.about,name='about'),
    path('contact_us/',views.contact_us,name='contact_us'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)