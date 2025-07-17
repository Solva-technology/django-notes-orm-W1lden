from django.urls import path

from . import views

urlpatterns = [
    path("", views.all_notes, name="all_notes"),
    path("user/<int:user_id>/", views.user, name="user"),
    path("users/", views.users, name="users"),
    path("note/<int:note_id>/", views.note_detail, name="note_detail"),
]
