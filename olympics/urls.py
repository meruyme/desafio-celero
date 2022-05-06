from django.urls import path

from olympics import views

app_name = 'olympics'

urlpatterns = [
    path('cities/', views.CityList.as_view()),
    path('cities/<int:pk>/', views.CityDetail.as_view()),
    path('sports/', views.SportList.as_view()),
    path('sports/<int:pk>/', views.SportDetail.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail.as_view()),
    path('games/', views.GamesList.as_view()),
    path('games/<int:pk>/', views.GamesDetail.as_view()),
    path('athletes/', views.AthleteList.as_view()),
    path('athletes/<int:pk>/', views.AthleteDetail.as_view()),
]
