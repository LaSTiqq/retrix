from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from .views import MainView
from .sitemaps import StaticSitemap
from django.urls import path

app_name = 'details'

sitemaps = {
    'static': StaticSitemap,
}

urlpatterns = [
    path('', MainView.as_view(), name='home'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('robots.txt', TemplateView.as_view(template_name='robots.txt', content_type="text/plain")),
]