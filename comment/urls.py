from django.urls import path
from comment import views


# Urls for comments
urlpatterns = [
    path('comments/', views.CommentList.as_view(), name="comments"),
    path('comments/<int:pk>/', views.CommentContent.as_view()),

]
