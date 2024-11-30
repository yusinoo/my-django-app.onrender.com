from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('accounts/', include('django.contrib.auth.urls')),  # Add built-in authentication
    path('', include('learning_logs.urls')),  # Your app's main URLs
]
