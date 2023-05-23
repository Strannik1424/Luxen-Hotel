from django.db import models
from django.urls import reverse


# Create your models here.
class ApartmentModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(null=True)
    img = models.ImageField(upload_to='media/', null=True)
    price = models.PositiveIntegerField(null=True)
    tags = models.ManyToManyField('Tags', null=True)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])
    

class Tags(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    


class Comment(models.Model):
    post = models.ForeignKey(ApartmentModel, on_delete=models.CASCADE, related_name='comments', null=True)
    # author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    # approved_comment = models.BooleanField(default=False)

    # def approve(self):
    #     self.approved_comment = True
    #     self.save()

    # def get_absolute_url(self):
    #     return reverse('post_detail', kwargs={'pk': self.post.pk})

    def __str__(self):
        return f'{self.post} |                               {self.name} | {self.email} | {self.created_date}'