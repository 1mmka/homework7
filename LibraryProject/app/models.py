from django.db import models
from app.validators import validate_integer

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=64)
    book_price = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=64)
    isbn = models.IntegerField()
    price = models.IntegerField(validators=[validate_integer])
    # если написать валидатор для book.price не надо будет писать для author.book_price
    author = models.ForeignKey(Author,on_delete=models.CASCADE,related_name='book',null=False,blank=False)

    def __str__(self):
        return self.title