from __future__ import unicode_literals

from django.db import models
from ..LogReg.models import User

# Create your models here.

class Poke(models.Model):
    poker = models.ForeignKey('LogReg.User', related_name="poker_key")
    poked = models.ForeignKey('LogReg.User', related_name="poked_key")
    created_at = models.DateTimeField(auto_now_add=True)
