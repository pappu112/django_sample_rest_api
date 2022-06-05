from django.urls import path

from . import views
# from .views import api_home


urlpatterns = [
    #path('', views.api_home), # localhost:8000/api/
    path('stuinfo/<int:pk>',views.student_details),
    path('stuinfo',views.all_student),
    path('add',views.student_create),
    path('student-api/',views.student_api),
]