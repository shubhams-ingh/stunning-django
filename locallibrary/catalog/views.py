from django.shortcuts import render
from .models import Book, Author, Genre, BookInstance

# Index view

def index(request):

	num_books = Book.objects.all.count()
	num_instances = BookInstance.objects.all.count()

	num_instances_avilable = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count()

	return render(
		request,
		'index.html',
		context={'num_books':num_books, 'num_instances':num_instances, 'num_instances_avilable':num_instances_avilable, 'num_authors':num_authors}
		)