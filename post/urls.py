from django.urls import path
from post import views

# Urls post
urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostContent.as_view()),
]
