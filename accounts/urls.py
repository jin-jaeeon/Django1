from django.urls import path
from . import views

# CBV
urlpatterns = [
    path('',views.index), 
    path('register/', views.register, name='register'),
    # path('<int:pk>/',views.PostDetail.as_view()),
]