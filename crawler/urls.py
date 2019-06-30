from django.urls import path, include
from . import views


urlpatterns = [
    path('crawling/<research>', views.crawling, name='crawling'),
]

