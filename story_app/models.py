from django.db import models
from django.contrib.auth.models import User
from mptt.models import MPTTModel, TreeForeignKey


class Story(MPTTModel):
    author = models.ForeignKey(User, related_name="stories", on_delete=models.CASCADE)
    title = models.CharField(max_length=150, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    details = models.TextField(null=True,blank=True)
    views = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class MPTTMeta:
        order_insertion_by = ['parent','title']

    def __str__(self):
        return self.title