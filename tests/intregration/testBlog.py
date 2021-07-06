from unittest import TestCase
from blog import Blog


class BlogTest(TestCase):
    def test_create_postIn_blog(self):
        b = Blog("Story", "Rahul Sen")
        b.create_post("Test Post", "Test Content")

        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, "Test Post")
        self.assertEqual(b.posts[0].content, "Test Content")

    def test_json(self):
        b = Blog("Story", "Rahul Sen")
        b.create_post("Test Post", "Test Content")

        expected = {
            "title": "Story",
            "author": "Rahul Sen",
            "Posts": [
                {
                 "title": "Test Post",
                 "content": "Test Content",
                }
            ]
        }

        self.assertEqual(expected, b.json())
