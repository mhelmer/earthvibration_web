import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse

from events.models import Event


def create_event(name, days, description, location, admission, published):
    """
    Creates an event with the given `name` taking place the given number of
    `days` offset to now (negative for events in the past,
    positive for upcoming events).
    """
    return Event.objects.create(name=name,
                                date=timezone.now()
                                + datetime.timedelta(days=days),
                                description=description, location=location,
                                admission=admission, published=published)


class EventViewTests(TestCase):
    def test_index_view_with_no_events(self):
        """
        If no events exist, appropriate messages should be displayed.
        """
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No upcoming events.")
        self.assertContains(response, "No past events.")

    def test_index_view_with_past_but_no_upcoming_events(self):
        """
        If no upcoming events exist, an appropriate message should be
        displayed.
        """
        create_event(name="Past event", days=-30,
                     description="A past event",
                     location="place", admission="0 SEK", published=True)
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No upcoming events.")

    def test_index_view_with_past_and_unpublished_upcoming_events(self):
        """
        If no published upcoming events exist, an appropriate message should be
        displayed.
        """
        create_event(name="Past event", days=-30,
                     description="A past event",
                     location="place", admission="0 SEK", published=True)
        create_event(name="Upcoming unpublished event", days=30,
                     description="An unpublished upcoming event",
                     location="place", admission="0 SEK", published=False)

        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No upcoming events.")

    def test_index_view_with_upcoming_but_no_past_events(self):
        """
        If no past events exist, an appropriate message should be displayed.
        """
        create_event(name="Upcoming event", days=30,
                     description="An upcoming event",
                     location="place", admission="0 SEK", published=True)
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No past events.")

    def test_index_view_with_upcoming_and_unpublished_past_events(self):
        """
        If no published past events exist, an appropriate message should be
        displayed.
        """
        create_event(name="Unpublished past event", days=-30,
                     description="An unpublished past event",
                     location="place", admission="0 SEK", published=False)
        create_event(name="Upcoming event", days=30,
                     description="An upcoming event",
                     location="place", admission="0 SEK", published=True)

        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No past events.")

    def test_index_view_with_unpublished_events(self):
        """
        If no events exist, appropriate messages should be displayed.
        """
        create_event(name="Upcoming unpublished event", days=30,
                     description="An unpublished upcoming event",
                     location="place", admission="0 SEK", published=False)
        create_event(name="Unpublished past event", days=-30,
                     description="An unpublished past event",
                     location="place", admission="0 SEK", published=False)

        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No upcoming events.")
        self.assertContains(response, "No past events.")
