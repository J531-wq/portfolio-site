"""
URL configuration for portfolio project.
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from portfolio_app import views   # adjust if your app name differs
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),          # homepage view
    path('contact/', views.contact_view, name='contact'),  # contact form handler
    path('success/', TemplateView.as_view(template_name="success.html"), name='success'),  # success page
]

# Serve media files in development
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
