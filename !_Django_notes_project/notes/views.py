from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import Note
from .forms import NoteForm
from django.contrib.auth.forms import UserCreationForm


def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправляем на страницу входа
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


@login_required
def note_list(request):
    notes = Note.objects.filter(user=request.user)
    return render(request, 'notes/note_list.html', {'notes': notes})


@login_required
def note_create(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.user = request.user
            note.save()
            return redirect('note_list')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})


@login_required
def note_update(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)  # Вместо .get() используем get_object_or_404()

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid():
            form.save()
            return redirect('note_list')
    else:
        form = NoteForm(instance=note)

    return render(request, 'notes/note_form.html', {'form': form})


@login_required
def note_delete(request, pk):
    note = get_object_or_404(Note, pk=pk, user=request.user)  # Безопасная проверка существования

    note.delete()
    return redirect('note_list')