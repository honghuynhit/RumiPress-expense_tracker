from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255, blank=True, null=True)
    authors = models.ManyToManyField(Author)
    publisher = models.CharField(max_length=255)
    published_date = models.DateField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    distribution_expense = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

class Expense(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.book.title} - {self.amount}"
