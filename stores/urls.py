from django.urls import path
from django.views.generic.base import TemplateView

from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

app_name='stores'

sitemaps = {
    'static': StaticViewSitemap
}

urlpatterns = [
    # ex: /polls/

    path('', views.index, name='index'),
    path('cu', views.cu, name='cu'),
    path('gs25', views.gs25, name='gs25'),
    path('7eleven', views.sel, name='7eleven'),
    path('ministop', views.ministop, name='ministop'),
    path('robots.txt', TemplateView.as_view(template_name='stores/robots.txt', content_type='text/plain'), name='robots_file'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),

    # path('oauth2callback', views.auth_return),
    # path('accounts/login', views.login, {'template_name': 'reports/login.html'}),
    # ex: /polls/5/
    # path('<int:question_id>/', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # path('<int:question_id>/results/', views.results, name='results'),
    # # ex: /polls/5/vote/
    # path('<int:question_id>/vote/', views.vote, name='vote'),
]
