from . import views
from django.urls import path
from django.conf.urls import handler404, handler500
# from .views import BlogList

from django.contrib.staticfiles.storage import staticfiles_storage
from django.urls import include, path
from django.views.generic.base import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.BlogList.as_view(), name='home'),
    path('', views.BlogList, name='home'),
    path('error', views.Error, name='error'),
    # path('search-blogs', views.BlogSearchView.as_view(), name = "search_blogs"),
    # path('footer', views.Footer, name='home'),
    path('<slug:slug>/', views.post_detail, name ='blog_single'),
     path(
        "ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
]

handler404 = views.custom_404
handler500 = views.custom_500