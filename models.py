import datetime

from django.db import models
from django.contrib.auth.models import User

class Domain(models.Model):
  """Domain class used to store domainis information.

  Add you domains here.
  """
  domain = models.CharField(max_length=150)
  active = models.BooleanField()

  def __unicode__(self):
    return self.domain

class Mailbox(models.Model):
  """Mailbox model."""
  email = models.CharField(max_length=250)
  password = models.CharField(max_length=250)
  quota = models.IntegerField(10)
  active = models.BooleanField(default=True)
  imap = models.BooleanField(default=True)
  pop3 = models.BooleanField(default=True)

  def __unicode__(self):
    return self.email

class Alias(models.Model):
  """Creates Aliases for Mailboxes."""
  source = models.CharField(max_length=255)
  destination = models.TextField()
  active = models.BooleanField()
	
  def __unicode__(self):
    return '%s --> %s' % (self.source, self.destination)
