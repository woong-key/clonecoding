from django.db import models

# Create your models here.
# ---------------------------------- [edit 21/04/19 김인웅] ---------------------------------- #
class Scene(models.Model):
    scene_subject = models.CharField(max_length=25, null=True, blank=True)
    scene_content = models.TextField()
    scene_datetime = models.DateTimeField()
    scene_password = models.CharField(max_length=4)
# ------------------------------------------------------------------------------------------- #
# ---------------------------------- [edit 21/04/20 김인웅] ---------------------------------- #
    def __str__(self):
        return self.scene_subject


