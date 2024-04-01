from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    
    # client folder urls
    path('', views.index, name='index'),
    
    # form folder urls
    path('progess_form/', views.progess_form, name='progess_form'),
    
    # destination folder urls
    path('main_destination_page/', views.main_destination_page, name='main_destination_page'),
    path('particular_destination_page/', views.particular_destination_page, name='particular_destination_page'),
    path('buhoma/', views.buhoma, name='buhoma'),
    path('bwindi/', views.bwindi, name='bwindi'),
    path('kidepo/', views.kidepo, name='kidepo'),
    path('murchison/', views.murchison, name='murchison'),
    path('mutanda/', views.mutanda, name='mutanda'),
    path('nkuringo/', views.nkuringo, name='nkuringo'),
    
    
    # experiences folder urls
    path('main_experience_page/', views.main_experience_page, name='main_experience_page'),
    path('particular_experience_page/', views.particular_experience_page, name='particular_experience_page'),
    path('intinerary/', views.intinerary, name='intinerary'),
    path('kidepo_intinerary/', views.kidepo_intinerary, name='kidepo_intinerary'),
    path('bwindi_intinerary/', views.bwindi_intinerary, name='bwindi_intinerary'),
    path('kigali_intinerary/', views.kigali_intinerary, name='kigali_intinerary'),
    path('kenya_intinerary/', views.kenya_intinerary, name='kenya_intinerary'),
    path('murchison_intinerary/', views.murchison_intinerary, name='murchison_intinerary'),
    path('boat_safari/', views.boat_safari, name='boat_safari'),
    path('game_drives/', views.game_drives, name='game_drives'),
    path('gorilla_trekking/', views.gorilla_trekking, name='gorilla_trekking'),
    path('guided_quad_bike/', views.guided_quad_bike, name='guided_quad_bike'),
    path('helicopter_safari/', views.helicopter_safari, name='helicopter_safari'),
    path('rhino_tracking/', views.rhino_tracking, name='rhino_tracking'),
        
    # blog folder urls
    path('main_blog_page/', views.main_blog_page, name='main_blog_page'),
    path('read_blog_page/', views.read_blog_page, name='read_blog_page'),
    
    # about folder urls
    path('main_about_page/', views.main_about_page, name='main_about_page'),
    path('our_team_page/', views.our_team_page, name='our_team_page'),
    path('read_about/', views.read_about, name='read_about'),
    path('our_impact/', views.our_impact, name='our_impact'),
    
    # read more folder urls
    path('read_more/', views.read_more, name='read_more'), 
    
    # Shop folder urls
    path('shop/', views.shop, name='shop'),
    
    # Admin Dashboard URL
    path('dashboard/', views.dashboard, name='dashboard'),
]