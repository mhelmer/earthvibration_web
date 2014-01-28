from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import RequestFactory
from django.core.urlresolvers import reverse
from django.utils import timezone

from blog.models import BlogEntry
from events.tests import create_event


def create_blog_entry(user, title, slug, content):
    return BlogEntry.objects.create(title=title, slug=slug, content=content,
                                    author=user)


def create_mock_blog_entry(user):
    title = 'Mock Title'
    slug = 'mock-slug'
    content = 'Mocking the content'
    return create_blog_entry(user, title, slug, content)


def create_future_published_event():
    return create_event(name="Upcoming event title", days=30,
                        description="An upcoming event description",
                        location="place", admission="0 SEK", published=True)


class AuthTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='User1', first_name='Firstname',
            email='myemail@domain.se', password='top_secret')


class AuthTestCaseTests(AuthTestCase):
    def test_user_create(self):
        #self.assertEqual(self.user.id, 1)
        self.assertEqual(self.user.username, 'User1')
        self.assertEqual(self.user.first_name, 'Firstname')
        self.assertEqual(self.user.email, 'myemail@domain.se')


class BlogIndexViewTests(AuthTestCase):
    def test_blog_entry_username(self):
        create_blog_entry(self.user, 'Title', 'title', 'No content')
        response = self.client.get(reverse('blog:index'))
        self.assertContains(response, self.user.username)
        self.assertContains(response, 'Title')


class BlogDetailsView(AuthTestCase):
    def test_details_has_full_content(self):
        title = 'Title'
        slug = 'title-slug'
        content = 'We have some content in this'
        entry = create_blog_entry(self.user, title, slug, content)
        response = self.client.get(entry.get_absolute_url())

        self.assertContains(response, self.user.username)
        self.assertContains(response, title)
        self.assertContains(response, content)

    def test_attached_entry_title(self):
        """
        Test fails but it shouldn't and it seems to work.
        Something must be broken with the test.
        """
        entry = create_mock_blog_entry(self.user)
        event = create_event(name="Upcoming event", days=30,
                             description="An upcoming event",
                             location="place", admission="0 SEK",
                             published=True)
        entry.attachment_object = event
        entry.save
        raise Exception('passing through')

        response = self.client.get(entry.get_absolute_url())
        self.assertContains(response, event.name)


class BlogEntryModelTests(AuthTestCase):
    def test_blog_entry_date_in_past(self):
        entry = create_blog_entry(self.user, 'Title', 'title', 'No content')
        self.assertTrue(entry.date_published <= timezone.now())
        self.assertTrue(entry.date_modified <= timezone.now())

    def test_blog_entry_save_sets_date_modified(self):
        entry = create_blog_entry(self.user, 'Title', 'title', 'No content')
        old_mod_date = entry.date_modified
        entry.save()
        self.assertTrue(old_mod_date < entry.date_modified)

    def test_attached_entry_title_change(self):
        entry = create_mock_blog_entry(self.user)
        event = create_future_published_event()
        entry.attachment_object = event
        entry.save()

        self.assertEqual(entry.attachment_object.name, event.name)
        event.name = "New name"
        event.save()
        self.assertEqual(entry.attachment_object.name, event.name)
