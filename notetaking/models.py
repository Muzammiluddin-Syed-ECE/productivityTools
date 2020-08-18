from django.db import models


# Create your models here.


class Subject(models.Model):
    subject_title = models.CharField(max_length=200)

    def __str__(self):
        return self.subject_title


class Chapter(models.Model):
    chapter_title = models.CharField(max_length=200)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.chapter_title


class Topic(models.Model):
    topic_title = models.CharField(max_length=200)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_title


class Definition(models.Model):
    definition_term = models.CharField(max_length=200)
    definition_text = models.CharField(max_length=1000)
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.definition_term


class Ideas(models.Model):
    idea_title = models.CharField(max_length=200)
    idea_text = models.CharField(max_length=1000)
    Topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.idea_title
