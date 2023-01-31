from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ProfileManager(models.Manager):
    pass


class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)
    nickname = models.CharField(max_length=50)

    objects = ProfileManager()

    def __str__(self):
        return self.nickname


class WordManager(models.Manager):
    pass


class Word(models.Model):
    normalized_word = models.TextField()
    synonyms = models.TextField()

    objects = WordManager()

    def __str__(self):
        return self.normalized_word


class DocumentManager(models.Manager):
    def get_file_text(self, file_id: int):
        return "Хуй"

    def get_synonyms(self, word: str):
        return "Хуй"

    def edit_word(self, file_id: int, replaced_word: str, new_word: str):
        return "Хуй"


class Document(models.Model):
    file = models.FileField(upload_to="documents/%Y/%m/%d")
    file_text = models.TextField()
    profile = models.ForeignKey(Profile, models.CASCADE, null=False)

    objects = DocumentManager()

    def __str__(self):
        return self.file.name
