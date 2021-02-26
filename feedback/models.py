from django.db import models


class feedback:
    ratings = models.IntegerField(default=0)
    words = models.CharField(max_length=300)
    time = models.DateTimeField()

    @property
    def __str__(self):
        return self.words