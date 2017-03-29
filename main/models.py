from django.db import models
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    slug = models.SlugField(blank=True,unique=True)
    updated = models.DateTimeField(auto_now=True,
                                   blank=True
                                   )
    timestamp = models.DateTimeField(auto_now_add=True,
                                     blank=True
                                     )

    def save(self, *args, **kwargs):
        if self.slug is None or self.slug == '':
            self.slug = slugify(self.title)
            qs_exists = Post.objects.filter(slug=self.slug).exists()
            if qs_exists:
                self.slug = "%s-%s" % (slugify(self.title), self.id)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse("main:detail",kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-timestamp','-updated']
