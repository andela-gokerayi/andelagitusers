import requests
from nose.tools import assert_true, assert_equal
from django.test import TestCase, Client
from django.core.urlresolvers import reverse_lazy

# Create your tests here.
class AndelaGitUsersTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = "https://api.github.com/orgs/andela/members"

# Test Views to check if we land correctly on homepage
class ViewsGitUserTestCase(AndelaGitUsersTestCase):

    def test_homepage_ok(self):
        response = self.client.get(reverse_lazy("homepage"))
        assert_equal(response.status_code, 200)

# Test if Api responds with ok code.
class GitFuncUsersTestCase(AndelaGitUsersTestCase):

    def test_api_return_ok(self):
        response = requests.get(self.url)
        assert_true(response.ok)

# Test if function script returns expected result

    def test_funct():
        pass
