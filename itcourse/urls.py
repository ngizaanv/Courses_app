from django.urls import path

from itcourse import views

urlpatterns = [
    path('courses', views.CourseList.as_view()),
    path('courses/<int:id>', views.CourseDetail.as_view()),
]

