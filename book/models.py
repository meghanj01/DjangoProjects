from django.db import models

# Create your models here.
class BooksModel(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    name = models.CharField(max_length=30, blank= False)
    publisher = models.CharField(max_length=20, blank= False)
    num_books = models.IntegerField()
    
    def __str__(self):
        return self.name + ' '+ self.publisher+ ' '+ self.num_books

    