from random import choice, randint

from django.core.management.base import BaseCommand

from main.factories import (
    CategoryFactory,
    TagFactory,
    UserFactory,
    PostFactory,
    create_unique_records
)


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            "--category-count",
            type=int,
            default=5,
            help="The number of categories to create"
        )
        parser.add_argument(
            "--tag-count",
            type=int,
            default=15,
            help="The number of tags to create"
        )
        parser.add_argument(
            "--post-count",
            type=int,
            default=3,
            help="The number of posts to create"
        )
        parser.add_argument(
            "--user-count",
            type=int,
            default=5,
            help="The number of users to create"
        )
        parser.add_argument(
            "--post-min-count",
            type=int,
            default=2,
            help="Minimum number of posts per user to create"
        )
        parser.add_argument(
            "--post-max-count",
            type=int,
            default=5,
            help="Maximum number of posts per user to create"
        )

    def handle(self, *args, **options):
        categories = create_unique_records(
            CategoryFactory, options["category_count"]
        )
        tags = create_unique_records(TagFactory, options["tag_count"])
        users = create_unique_records(UserFactory, options["user_count"])

        for user in users:
            post_counter = 0
            post_count = randint(
                options["post_min_count"], options["post_max_count"] + 1
            )
            while post_counter < post_count:
                post_category = choice(categories)
                tag_count = randint(2, 6)

                k = 0
                post_tags = []
                while k < tag_count:
                    post_tags.append(choice(tags))
                    k += 1

                post = create_unique_records(
                    PostFactory, 1, category=post_category, author=user
                )[0]

                post.tags.add(*post_tags)
                post.save()
                print(post, post.tags.all())
                
                post_counter += 1

