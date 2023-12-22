from django.test import TestCase

from django.test import RequestFactory, TestCase

# check models

from .views import *
from .models import *


class PostTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(title="title", text="text")

    def test_title_matches_expected_title(self):
        expected_title = "title"
        self.assertEqual(self.post.title, expected_title)

    def test_text_matches_expected_text(self):
        expected_text = "text"
        self.assertEqual(self.post.text, expected_text)

    def test_updated_text_matches_expected_text(self):
        self.post.text = "awesome"
        expected_text = "awesome"
        self.assertEqual(self.post.text, expected_text)
