from django.db import models

# Create your models here.
class History(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='histories')
    query = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.query


