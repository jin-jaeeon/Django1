from django.urls import path
from . import views

# CBV
urlpatterns = [
    path('',views.login_view, name='login-view'), 
    path('register/', views.register_view, name='register'),
    # path('<int:pk>/',views.PostDetail.as_view()),
]