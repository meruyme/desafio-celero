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
    path('events/', views.EventList.as_view()),
    path('events/<int:pk>/', views.EventDetail.as_view()),
    path('athletes_games/', views.AthleteGameList.as_view()),
    path('athletes_games/<int:pk>/', views.AthleteGameDetail.as_view()),
    path('athletes_games_events/', views.AthleteGameEventList.as_view()),
    path('athletes_games_events/<int:pk>/', views.AthleteGameEventDetail.as_view()),
]
