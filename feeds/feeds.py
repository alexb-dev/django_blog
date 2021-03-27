from django.contrib.syndication.views import Feed
from django.urls import reverse
from blogging.models import Post
from django.urls import reverse

class LatestEntriesFeed(Feed):
    title = "Latests posts"
    link = "latest/feed/"
    description = "Latest post from django blog"

    def items(self):
        return Post.objects.all()[:5]


    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text

