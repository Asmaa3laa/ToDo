from django.db import models
from django.contrib.auth.models import User
import json
from json import JSONEncoder


class Agenda(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='UserID')
    # created = models.DateTimeField()
    content = models.CharField(max_length=200)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.content

    class EmployeeEncoder(JSONEncoder):
        def default(self, o):
            return o.__dict__