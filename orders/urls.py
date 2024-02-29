from django.urls import path

from . import views

urlpatterns = [
    path("", views.loginpage, name="loginpage"),
    path('login/', views.validateuser, name='validateuser'),
    path('register/', views.signup_view,name='signup_view'),
    path('home/', views.homepage, name='homepage' ),
    path('logout/', views.logout_view, name='logout_view'),
    path('addnote/', views.create_note, name='create_note'),
    path('deletenote/<int:note_id>/', views.delete_note, name='delete_note')
]