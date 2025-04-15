from django.db import models

# Create your models here.
class TitleRequest(models.Model):
    content = models.TextField(help_text="The blog post content")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Title request {self.id} at {self.created_at}"
