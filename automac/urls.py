from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home),
    path('xyz',views.profile),
    path('getstat1/<str:pk>',views.getLight1,name='getstat1'),
    path('getstat2/<str:pk>',views.getLight1,name='getstat2'),
    path('getstat3/<str:pk>',views.getLight1,name='getstat3'),
    path('getstat4/<str:pk>',views.getLight1,name='getstat4'),
    path('switch1/<str:pk>',views.ToggleLight1,name='on1'),
    path('switch2/<str:pk>',views.ToggleLight2,name='on2'),
    path('switch3/<str:pk>',views.ToggleLight3,name='on3'),
    path('switch4/<str:pk>',views.ToggleLight4,name='on4'),
    path('ctrl/<str:pk>',views.sendControl,name='control'),
]
