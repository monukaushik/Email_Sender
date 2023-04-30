from django.contrib import admin
from django.urls import path
from Email_App import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.home ),
    path('send/',views.emailsend, name='send'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
