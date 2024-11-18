from django.urls import path
from post import views


urlpatterns = [
    path('explore-new/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostContent.as_view()),
]