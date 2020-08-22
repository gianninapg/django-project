from django.db import models


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    content = models.TextField()
    image_url = models.CharField(max_length=200, default='https://www.sl-inspiration.com/2014/08/creating-anumated-gifs-for-second-life.html')
