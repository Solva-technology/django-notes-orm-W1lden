from django.http import HttpResponse
from django.shortcuts import render

from .models import Note, User


def all_notes(request):
    notes = Note.objects.select_related("author", "status").prefetch_related("categories").all()
    return render(request, "all_notes.html", {"notes": notes})


def user(request, user_id):
    user = User.objects.select_related(
        "userprofile"
        ).prefetch_related("note_set", "note_set__status").get(id=user_id)
    return render(request, "user.html", {"user": user})

def users(request):
    users = User.objects.all()
    return render(request, "users.html", {"users": users})

def note_detail(request, note_id):
    note = Note.objects.select_related(
        "author__userprofile", 
        "status"
        ).prefetch_related(
            "categories"
            ).get(id=note_id)
    return render(request, "note_detail.html", {"note": note})