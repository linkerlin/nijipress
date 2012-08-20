import base
import utils.escape
import models
from urlparse import urlparse

RSS_ITEMS_COUNT = 16

def rss_post(post, url):
    post.plain_title = utils.escape.esc_title_plain(post.title)
    post.ident = ''.join([url.scheme, '://', url.netloc, '/?p=', str(post.pid)])
    post = utils.escape.client_post(post)
    return post

def rss_posts(origin_posts, url):
    return map(lambda p: rss_post(p, url), origin_posts)

class Build(base.BaseView):
    def get(self):
        url = urlparse(self.request.url)
        self.put_page('templates/feed.xml', {
            'site_link': url.scheme + '://' + url.netloc,
            'posts': rss_posts(models.post.fetch(0, RSS_ITEMS_COUNT), url),
        })
