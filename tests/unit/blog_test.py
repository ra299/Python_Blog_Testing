from unittest import TestCase
from blog import Blog

class BlogTest(TestCase):
    def test_create_blog(self):
        b = Blog("Story", "Rahul Sen")

        self.assertEqual("Story", b.title)
        self.assertEqual("Rahul Sen", b.author)

        # asertListEqual for List purpose
        self.assertListEqual([], b.posts)

    def test_json(self):
        b = Blog("Story", "Rahul Sen")

        expected = {
            "title": "Story",
            "author": "Rahul Sen"
        }
        self.assertDictEqual(expected, b.json())

    def test_repr(self):
        b = Blog("Story", "Rahul Sen")
        b2 = Blog("My Day", "Rolf")
        self.assertEqual(b.__repr__(), "Story by Test Rahul Sen(0 Posts)")
        self.assertEqual(b2.__repr__(), "My Day by Test Rolf(0 Posts)")

    def test_repr_multiple_post(self):
        b = Blog("wakeUp", "Amme")
        b.posts = ["post1", "post2", "post3", "post4"]

        self.assertEqual(b.__repr__(), "wakeUp by Amme (4 posts)")

