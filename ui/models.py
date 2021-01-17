from django.db import models


class History(models.Model):
    verb = models.CharField(max_length=50)
    noun = models.CharField(max_length=50, default='')
    proper_noun = models.BooleanField(default=False)
    question = models.BooleanField(default=False)
    negative = models.BooleanField(default=False)
    affix = models.CharField(max_length=10)
    morph = models.CharField(max_length=10)
    tense = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.verb

    class Meta:
        verbose_name_plural = 'History'
