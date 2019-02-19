from django.db import models


class AuthKey(models.Model):
    key = models.CharField(max_length=40, null=False)

    def __str__(self):
        return "{}".format(self.key)
