from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    changefreq = 'daily'
    priority = 0.5

    def items(self):
        return ['stores:cu', 'stores:gs25', 'stores:7eleven', 'stores:ministop']

    def location(self, item):
        return reverse(item)
