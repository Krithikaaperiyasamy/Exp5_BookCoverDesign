from django.shortcuts import render

def home(request):
    return render(request, 'book_app/book.html')  # include app folder name

