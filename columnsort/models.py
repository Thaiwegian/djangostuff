import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class AddressList(BaseModel):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.first} {self.last}'

    class Meta:
        ordering = ['first', 'last']

