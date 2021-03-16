from django.urls import path
from tutorial_api.views import AuthorView


urlpatterns = [
    path('authors/', AuthorView.as_view(),),
    path('authors/<int:aid>', AuthorView.as_view(),),
]