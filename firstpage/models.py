from django.db import models

# Create your models here.
# ---------------------------------- [edit 21/04/19 김인웅] ---------------------------------- #
class Story(models.Model):
    story_subject = models.CharField(max_length=25)
    story_content = models.TextField()
    story_datetime = models.DateTimeField()
    story_password = models.CharField(max_length=4)
# ------------------------------------------------------------------------------------------- #
# ---------------------------------- [edit 21/04/20 김인웅] ---------------------------------- #
    def __str__(self):
        return self.story_subject