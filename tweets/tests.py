from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tweet

User = get_user_model()


class TestHomeView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="tester", password="testpassword")
        self.client.login(username="tester", password="testpassword")
        self.url = reverse("tweets:home")

        self.tweet = Tweet.objects.create(user=self.user, content="this is a tweet")

    def test_success_get(self):
        response = self.client.get(self.url)
        tweets_db = Tweet.objects.all()
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tweets/home.html")
        self.assertQuerysetEqual(response.context["tweets"], tweets_db)


# class TestTweetCreateView(TestCase):
#     def test_success_get(self):

#     def test_success_post(self):

#     def test_failure_post_with_empty_content(self):

#     def test_failure_post_with_too_long_content(self):


# class TestTweetDetailView(TestCase):
#     def test_success_get(self):


# class TestTweetDeleteView(TestCase):
#     def test_success_post(self):

#     def test_failure_post_with_not_exist_tweet(self):

#     def test_failure_post_with_incorrect_user(self):


# class TestLikeView(TestCase):
#     def test_success_post(self):

#     def test_failure_post_with_not_exist_tweet(self):

#     def test_failure_post_with_liked_tweet(self):


# class TestUnLikeView(TestCase):

#     def test_success_post(self):

#     def test_failure_post_with_not_exist_tweet(self):

#     def test_failure_post_with_unliked_tweet(self):
