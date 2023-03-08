from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('account/login/', CustomLoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('account/register/', RegisterPage.as_view(), name='register'),
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
