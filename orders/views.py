from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.decorators import login_required


# Create your views here.

def loginpage(request):
    return render(request, 'login.html',{})

def homepage(request):
    if request.user.is_authenticated:
        notes = Note.objects.filter(user=request.user)
        return render(request, 'index.html',{'notes':notes})
    return render(request, '404.html',{})

def validateuser(request):
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('/home/')

    else:
        return render(request, 'failed_login.html',{})


def signup_view(request):
    if request.method == 'POST':
        username = request.POST['set_username']
        password = request.POST['set_password']

        # Create a new user object
        new_user = User.objects.create_user(username=username, password=password)

        return redirect('/')

    return render(request,'createuser.html',{})


def logout_view(request):
    logout(request)
    return redirect('/')

@login_required
def create_note(request):
    if request.method == 'POST' and request.user.is_authenticated:
        content = request.POST.get('content')
        title = request.POST.get('title')

        if content:
            # Associate the note with the logged-in user
            note = Note.objects.create(user=request.user, content=content, title=title)
            return redirect('/home/')

    return HttpResponse('Improper content')

@login_required
def user_notes(request):
    # Fetch all notes for the logged-in user
    notes = Note.objects.filter(user=request.user)

    return render(request, 'index.html', {'notes': notes})

@login_required
def delete_note(request, note_id):
    note = get_object_or_404(Note, id=note_id, user=request.user)
    note.delete()
    return redirect('/home/')