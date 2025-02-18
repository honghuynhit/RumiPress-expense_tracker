import os
import csv
import uuid  # For generating unique IDs
from datetime import datetime
from django.core.management.base import BaseCommand
from expense_tracker.models import Book, Author, Category

class Command(BaseCommand):
    help = "Import books data from a CSV file"

    def generate_unique_id(self):
        """Generate a new unique ID using UUID"""
        return str(uuid.uuid4().int)[:13]  # Shorten UUID to fit within max_length=20

    def handle(self, *args, **kwargs):
        file_path = os.path.join("data", "Books Distribution Expenses - Books.csv")  

        if not os.path.exists(file_path):
            self.stdout.write(self.style.ERROR(f"File not found: {file_path}"))
            return

        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                try:
                    # Convert date format from MM/DD/YYYY to YYYY-MM-DD
                    published_date = datetime.strptime(row["published_date"], "%m/%d/%Y").date()

                    category, _ = Category.objects.get_or_create(name=row["category"])

                    # Handle multiple authors
                    author_names = [name.strip() for name in row["authors"].split(",")]
                    author_objects = []
                    for name in author_names:
                        author, _ = Author.objects.get_or_create(name=name)
                        author_objects.append(author)

                    # Check if the book ID already exists
                    book_id = row["id"]
                    if Book.objects.filter(id=book_id).exists():
                        book_id = self.generate_unique_id()  # Generate a new unique ID

                    # Create book entry
                    book = Book.objects.create(
                        id=book_id,
                        title=row["title"],
                        subtitle=row["subtitle"],
                        publisher=row["publisher"],
                        published_date=published_date,
                        category=category,
                        distribution_expense=row["distribution_expense"]
                    )

                    # Assign authors to the book
                    book.authors.set(author_objects)

                    self.stdout.write(self.style.SUCCESS(f"Book '{book.title}' imported successfully with ID: {book_id}"))

                except Exception as e:
                    self.stdout.write(self.style.ERROR(f"Error importing row {row}: {e}"))
