from django.urls import path
from app.views import get_user_data, home, recommendation, comment
urlpatterns = [

 path('user-data/<int:id>/', get_user_data, name="user_data"), 
 path('', home, name="home"), 
 path('recommendation/', recommendation, name="recommendation"),
 path('comment/', comment, name="recommendation"),
 
 
]
