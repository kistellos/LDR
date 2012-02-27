from django.db import models

# Create your models here.

class LanguageObject(models.Model):
    article = models.CharField(max_length=20, blank=True, null=True)
    phrase = models.TextField()
    translation = models.TextField()
    tags = models.TextField(blank=True, null=True)
    example = models.TextField(blank=True, null=True)
    other_forms = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return '%s %s' % (self.article, self.phrase)
# 
#    TYPE_CHOICES = (
#        ('NO', 'noun'),
#        ('VE', 'verb'),
#        ('AD', 'adjective'),
#        ('EX', 'exclamation'),
#        ('PH', 'phrase')
#
#    )
#    type = models.CharField(max_length=2, choices=TYPE_CHOICES)
