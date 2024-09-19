from django.urls import path
from . import views

# CBV
urlpatterns = [
    path('',views.index), 
    # path('<int:pk>/',views.PostDetail.as_view()),
]