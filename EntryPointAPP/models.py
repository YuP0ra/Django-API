from django.db import models


class APICall(models.Model):
    user = models.CharField(max_length=30, null=False)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)
