from django.urls import path
from . import views

urlpatterns = [
    path('info_view/', views.stud_info_view),
    path('info_view/<int:roll_no>', views.stud_detail_view),
    path('info_view/detail_info_view/<int:roll_no>/', views.studinfo_detail_view),
    path('info_search/', views.stud_search_view),
    path('create/', views.stud_create_form),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('register/', views.register_view),
]