from django.shortcuts import render
from app.models import Author,Book

# Create your views here.
def get_data(request):
    authors = Author.objects.all()
    books = Book.objects.all()

    for author in authors:
        author.book_price = 0
        for book in books:
            if book.author.name == author.name:
                author.book_price += book.price
        author.save()
    '''при каждом запуске суммы всех книг автора оставались такими же и опять суммировались
        поэтому я решил обнулить счет и заново пересчитать если были какие то изменения'''

    context = {'data':authors}

    return render(request,template_name='data.html',context=context)