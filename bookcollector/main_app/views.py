from django.shortcuts import render, redirect
from .models import Book , Reader, Rating

from .forms import RatingForm
# Add the following import


# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def books_index(request):
  books = Book.objects.all()
  return render(request, 'books/index.html', { 'books': books })



def books_detail(request, book_id):
  book = Book.objects.get(id=book_id)
  noreader = Reader.objects.exclude(id__in = book.reader.all().values_list('id') )
  rating_form = RatingForm()
  return render(request, 'books/detail.html', { 'book': book, 
  'rating_form' : rating_form,
  'noreaders' : noreader})

def add_rating(request, book_id):
  # create the ModelForm using the data in request.POST
  form = RatingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_adding = form.save(commit=False)
    new_adding.book_id = book_id
    new_adding.save()
  return redirect('detail', book_id=book_id)

