from django.db import models


# Create your models here.
class Newsletter(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name


class Subscriber(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=1024)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    newsletters = models.ManyToManyField(Newsletter, through="Subscription")

    def __str__(self) -> str:
        return self.name


class Subscription(models.Model):
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.newsletter.name + ' subscribed to ' + self.subscriber.name
    

class Issue(models.Model):
    content = models.TextField()
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    newsletter = models.ForeignKey(Newsletter, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title