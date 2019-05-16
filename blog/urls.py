
from django.conf.urls import url
from .views import (
    article_create_view
)


urlpatterns = [
   url('create-article/$', article_create_view, name='create_article'),
]
