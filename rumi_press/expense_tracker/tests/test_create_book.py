from django.test import TestCase
from expense_tracker.models import Book, Author, Category
from datetime import date

class BookModelTest(TestCase):
    def setUp(self):
        """Set up required objects before running tests"""
        self.category = Category.objects.create(name="Business Analytics")
        self.author = Author.objects.create(name="Jay Liebowitz")

    def test_create_book(self):
        """Test book creation and saving to the database"""
        book = Book.objects.create(
            id="9781466596092",
            title="Business Analytics",
            subtitle="An Introduction",
            publisher="CRC Press",
            published_date=date(2013, 12, 19),
            category=self.category,
            distribution_expense=5.60
        )
        book.authors.add(self.author)  # Adding ManyToMany field

        # Retrieve book from DB
        saved_book = Book.objects.get(id="9781466596092")

        # Assertions
        self.assertEqual(saved_book.title, "Business Analytics")
        self.assertEqual(saved_book.publisher, "CRC Press")
        self.assertEqual(saved_book.published_date, date(2013, 12, 19))
        self.assertEqual(saved_book.category.name, "Business Analytics")
        self.assertAlmostEqual(float(saved_book.distribution_expense), 5.60)
        self.assertIn(self.author, saved_book.authors.all())
