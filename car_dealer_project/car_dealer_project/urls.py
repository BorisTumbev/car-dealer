
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.views.generic.base import TemplateView
from django.conf import settings
from django.conf.urls.static import static
#from django.conf.urls import handler404

urlpatterns = [
    #path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('admin/', admin.site.urls),
    path('', include('car_dealer_app.urls')),
    path('', include('users_app.urls')),
    path('', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



#custom 404 error
handler404 = "car_dealer_app.utils.error_404"
