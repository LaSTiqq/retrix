from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .views import send
from .sitemaps import LatvianSitemap, EnglishSitemap, RussianSitemap
from django.urls import path

app_name = 'details'

sitemaps = {
    'latvian': LatvianSitemap,
    'english': EnglishSitemap,
    'russian': RussianSitemap,
}

urlpatterns = [
    path('', send, name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
]