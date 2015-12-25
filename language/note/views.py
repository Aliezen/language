from django.shortcuts import render

# Create your views here.
def note(request):
    return render(request, 'note/note.html')

def MyNotesOnline(request):
    return render(request, 'note/MyNotesOnline.html')