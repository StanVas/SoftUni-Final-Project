from django.test import TestCase
from django.urls import reverse

from tattoo_web.articles.models import Article
from tattoo_web.photos.models import ArtistPhoto


class HomeViewTests(TestCase):
    VALID_ARTICLE_DATA = {
        'title': 'TestTitle',
        'sub_title': 'TestSubtitle TestSubtitle TestSubtitle',
        'main_image': 'images/small.gif',
        'secondary_image': 'images/small.gif',
        'extra_image': 'images/small.gif',
        'byline': 'TestByline',
        'main_text': 'TestMainText',
        'conclusion': 'TestConclusion',
    }

    VALID_PHOTO_DATA = {
        'photo': 'images/small.gif',
        'description': 'TestDescription',
    }

    def test_home_page__no_articles__no_photos(self):
        response = self.client.get(
            reverse('home'),
        )

        context = response.context

        self.assertEqual(200, response.status_code)

        self.assertEqual(context['latest_articles'].count(), 0)
        self.assertEqual(context['latest_images'].count(), 0)

        self.assertTemplateUsed(response, 'common/home.html', 'base/base.html')

    def test_home_page__one_article__one_photo(self):
        test_article = Article.objects.create(**self.VALID_ARTICLE_DATA)

        test_photo = ArtistPhoto.objects.create(**self.VALID_PHOTO_DATA)

        test_article.save()
        test_photo.save()

        response = self.client.get(
            reverse('home'),
        )

        context = response.context

        self.assertEqual(context['latest_articles'].count(), 1)
        self.assertEqual(context['latest_images'].count(), 1)
