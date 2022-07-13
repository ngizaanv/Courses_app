from django.urls import path

from itcourse import views

urlpatterns = [
    path('courses/', views.CourseList.as_view(), name='get_post_course'),
    path('courses/<int:pk>/', views.CourseDetail.as_view(), name='get_delete_course'),
]

