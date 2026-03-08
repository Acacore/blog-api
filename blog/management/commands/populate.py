import uuid
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from blog.models import Category, Post
User = get_user_model()

class Command(BaseCommand):
    help = "Seeds the database with Admin, Staff, Categories, and Posts"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_LABEL("--- Starting Database Seeding ---"))

        # 1. Verify Admin exists
        try:
            admin = User.objects.get(is_superuser=True)
            self.stdout.write(f"Confirmed Superuser: {admin.username}")
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("Error: No superuser found. Run 'python manage.py createsuperuser' first."))
            return

        # 2. Ensure Staff User exists (The author for our posts)
        staff_user, created = User.objects.get_or_create(
            username="staff_writer",
            defaults={
                "email": "writer@blogflow.com",
                "role": "STAFF",
                "is_staff": True,
                "bio": "Professional backend blogger."
            }
        )
        if created:
            staff_user.set_password("password123")
            staff_user.save()
            self.stdout.write(self.style.SUCCESS("Created Staff User: staff_writer"))

        # 3. Define Data Map: Category -> List of Post Titles
        data_map = {
            "General": ["Daily Community Updates", "Local Town Hall Highlights"],
            "Politics": ["New Policy Reform Announced", "Election Season Preparations"],
            "World": ["Global Climate Summit Outcomes", "International Trade Agreements"],
            "Technology": ["The Rise of AI in 2026", "Why Backend Engineering Matters"],
            "Lifestyle": ["10 Tips for a Balanced Work Life", "Exploring Urban Architecture"],
            "Entertainment": ["Top 10 Must-Watch Movies", "The Evolution of Music Streaming"],
            "Sports": ["Championship Finals Recap", "Training for Your First Marathon"]
        }

        # 4. Loop through the Map to create Categories and then their Posts
        for cat_name, post_titles in data_map.items():
            # Create Category (Slug is handled by get_or_create defaults)
            category, cat_created = Category.objects.get_or_create(
                name=cat_name,
                defaults={'slug': slugify(cat_name)}
            )
            
            if cat_created:
                self.stdout.write(self.style.SUCCESS(f"Created Category: {cat_name}"))

            # Create Posts for this specific category
            for title in post_titles:
                post, post_created = Post.objects.get_or_create(
                    title=title,
                    author=staff_user,
                    defaults={
                        "content": f"This is the official content for {title}. It covers the latest trends in {cat_name}.",
                        "category": category,
                        "status": "published"
                    }
                )
                if post_created:
                    self.stdout.write(f"  - Created Post: {title}")

        self.stdout.write(self.style.SUCCESS("\n--- Database Population Complete! ---"))