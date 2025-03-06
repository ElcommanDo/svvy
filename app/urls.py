from django.urls import path
from app.views import get_user_data, home, login_view
urlpatterns = [

 path('user-data/<int:id>/', get_user_data, name="user_data"), 
 path('', home, name="home"), 
 path('login/', login_view, name="login"),
 
 
 
]
