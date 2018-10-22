from __future__ import unicode_literals
from django.db import models

from apps.users_app.models import User


class WishManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        ### ITEM VALIDATION ###
        if len(postData['item']) == 0:
            errors["item"] = "Item must be entered"
        elif len(postData['item']) < 3:
            errors["item"] = "Item must be at least 3 characters"
        elif len(postData['item']) > 254:
            errors["item"] = "Woah there! That's a really long item"

        ### ITEM VALIDATION ###
        if len(postData['description']) == 0:
            errors["description"] = "Description must be entered"
        elif len(postData['description']) < 3:
            errors["description"] = "Description must be at least 3 characters"
        elif len(postData['description']) > 254:
            errors["description"] = "Woah there, greedy! That's a really long description"

        return errors


# Create your models here.
class Wish(models.Model):
    item = models.CharField(max_length=250)
    description = models.CharField(max_length=255)
    wisher = models.ForeignKey(User, related_name = "wishes")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    granted_at = models.DateTimeField(null=True, blank=True)

    objects = WishManager()
    def __repr__(self):
        return "<Wish object: {} {}>".format(self.id, self.item)
