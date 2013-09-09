from markdown import markdown
import datetime
from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User
from django.contrib import admin

VIEWABLE_STATUS = [3, 4]

class ViewableManager(models.Manager):
    def get_query_set(self):
        default_queryset = super(ViewableManager, self).get_query_set()
        return default_queryset.filter(status__in=VIEWABLE_STATUS)

class Category(models.Model):
    """A content category"""
    label = models.CharField(blank=True, max_length=50)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "categories"

    def __unicode__(self):
        return self.label

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('label',)}

admin.site.register(Category, CategoryAdmin)

class Story(models.Model):
    """A hunk of content for our site, generally corresponding to a page"""
    
    STATUS_CHOICES = (
        (1, "Needs Edit"), 
        (2, "Needs Approval"), 
        (3, "Published"),
        (4, "Archived"),
    )

    title = models.CharField(max_length=100)
    slug = models.SlugField()
    category = models.ForeignKey(Category)
    markdown_content = models.TextField()
    html_content = models.TextField(editable=False)
    owner = models.ForeignKey(User)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    created = models.DateTimeField(default=datetime.datetime.now)
    modified = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        ordering = ['modified']
        verbose_name_plural = "stories"

    @permalink
    def get_absolute_url(self):
        return ("cms-story", (), {'slug': self.slug})

    def save(self):
        self.html_content = markdown(self.markdown_content)
        self.modified = datetime.datetime.now()
        super(Story, self).save()

    admin_objects = models.Manager()
    objects = ViewableManager()


class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'status', 'created', 'modified')
    search_fields = ('title', 'content')
    list_filter = ('status', 'owner', 'created', 'modified')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Story, StoryAdmin)
