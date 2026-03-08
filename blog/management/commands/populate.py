import uuid
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from django.contrib.auth import get_user_model
from blog.models import Category, Post, Comment
User = get_user_model()


class Command(BaseCommand):
    help = "Seeds the database with Users, Categories, Posts, and 140 Comments"

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_LABEL("--- Starting Comprehensive Seeding ---"))

        # 1. Ensure Staff User exists
        staff_user, _ = User.objects.get_or_create(
            username="staff_writer",
            defaults={"email": "writer@blogflow.com", "role": "STAFF", "is_staff": True}
        )
        if _:
            staff_user.set_password("password123")
            staff_user.save()

        # 2. Create a Pool of 10 Regular Users
        commenting_users = []
        for i in range(1, 11):
            user, created = User.objects.get_or_create(
                username=f"user_{i}",
                defaults={"email": f"user{i}@example.com", "role": "USER"}
            )
            if created:
                user.set_password("password123")
                user.save()
            commenting_users.append(user)
        self.stdout.write(self.style.SUCCESS(f"Verified 10 commenting users."))

        # 3. Data Map for Categories and Posts
        data_map = {
            "General": ["Daily Community Updates", "Local Town Hall Highlights"],
            "Politics": ["New Policy Reform Announced", "Election Season Preparations"],
            "World": ["Global Climate Summit Outcomes", "International Trade Agreements"],
            "Technology": ["The Rise of AI in 2026", "Why Backend Engineering Matters"],
            "Lifestyle": ["10 Tips for a Balanced Work Life", "Exploring Urban Architecture"],
            "Entertainment": ["Top 10 Must-Watch Movies", "The Evolution of Music Streaming"],
            "Sports": ["Championship Finals Recap", "Training for Your First Marathon"]
        }

        # 4. Seed Categories, Posts, and 10 Comments per Post
        sample_comments = [
            "Great insights, thanks for sharing!",
            "I found this very helpful for my current project.",
            "Interesting perspective, but I slightly disagree with the second point.",
            "Can you provide more details on this?",
            "Exactly what I was looking for today.",
            "Nicely written and very easy to follow.",
            "Does this apply to small-scale systems too?",
            "Bookmarking this for later. Thanks!",
            "I'd love to see a follow-up post on this topic.",
            "Solid explanation of a complex subject."
        ]

        for cat_name, post_titles in data_map.items():
            category, _ = Category.objects.get_or_create(name=cat_name, defaults={'slug': slugify(cat_name)})
            
            for title in post_titles:
                post, post_created = Post.objects.get_or_create(
                    title=title,
                    author=staff_user,
                    defaults={
                        "content": f"Content for {title} in {cat_name}.",
                        "category": category,
                        "status": "published"
                    }
                )

                # 5. Create 10 unique comments for every post
                # We use get_or_create on content + post + author to avoid duplicates
                for i in range(10):
                    Comment.objects.get_or_create(
                        post=post,
                        author=commenting_users[i],
                        defaults={"content": sample_comments[i]}
                    )
                
                if post_created:
                    self.stdout.write(f"  - Created Post & 10 Comments: {title}")

        self.stdout.write(self.style.SUCCESS("\n--- Seeding Complete: 14 Posts and 140 Comments! ---"))