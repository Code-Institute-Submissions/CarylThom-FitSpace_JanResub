from django.db import models


class Newsletter(models.Model):
    """ Newsletter fields """

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
