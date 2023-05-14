from django.db import models


class categoriesModel(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(
        upload_to=
        "files")
    color = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class podcastModel(models.Model):

    channel = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    description = models.TextField()
    cover_pic = models.ImageField(
        upload_to=
        "files/")
    speaker = models.CharField(max_length=50)
    TYPE_CHOICES = (('V', 'Video'), ('A', 'Audio'))
    type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    category = models.CharField(max_length=50)
    media = models.FileField(
        upload_to=
        "files/")

    def __str__(self):
        return self.channel
