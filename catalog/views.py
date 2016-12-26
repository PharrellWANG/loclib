from django.shortcuts import render

from .models import BookInstance, Book, Author, Genre


# Create your views here.
def index(request):
    """
        View function for home page of site.
        """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.
    num_genres = Genre.objects.count()
    num_LearningwithKernels = BookInstance.objects.filter(book__title__startswith='Learning').count()

    # Render the HTML template base_generic.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_LearningwithKernels': num_LearningwithKernels, 'num_genres': num_genres, 'num_books': num_books,
                 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors},
        # the context is a dictionary
    )
