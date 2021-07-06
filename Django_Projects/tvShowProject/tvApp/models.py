from django.db import models

class ShowsManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        if len(post_data['title']) < 1:
            errors['title'] ="Title must be entered"
    
        if len(post_data['network']) < 1:
            errors['network'] = "Network must be entered"
    
        if len(post_data['release_date']) < 1:
            errors['release_date'] = "Release date must be entered"
    
        if len(post_data['description']) < 1:
            errors['description'] = "Description must be entered"
    
        return errors

class Shows(models.Model):
    title = models.CharField(max_length=45)
    network = models.CharField(max_length=45)
    release_date = models.DateField(null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ShowsManager()