from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.
class DocxFile(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        get_user_model(), null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title