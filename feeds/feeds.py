from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post
from django.urls import reverse

from django.utils.feedgenerator import Rss201rev2Feed

class CorrectMimeTypeFeed(Rss201rev2Feed):
    content_type = 'application/xml; charset=utf-8'

class LatestEntriesFeed(Feed):
    feed_type = CorrectMimeTypeFeed
    title = "Latests 5 posts"
    link = "latest/feed/"
    description = "Latest post from django blog"

    def items(self):
        # return Post.objects.all()[:5]
        return Post.objects.order_by('-created_date')[:5]


    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

