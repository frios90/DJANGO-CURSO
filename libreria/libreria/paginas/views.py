from django.shortcuts import render
from book.models import Book,File

def inicio (request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, "paginas/inicio.html", context)


def libro (request, b_id):
    print("aqui en el libro")
    book = Book.objects.get(id=b_id)
    print(b_id)
    files = File.objects.filter(book_id=b_id)
    context = {'book': book, 'files': files}
    print(context)
    return render(request, "paginas/libro.html", context)