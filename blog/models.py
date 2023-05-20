from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

STATUS = (
    (0,"Draft"),
    (1,"Publish")
)

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_post')
    updated_on = models.DateTimeField(auto_now= True)
    content = RichTextUploadingField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now= True)
    status = models.IntegerField(choices=STATUS, default=0)
    image = models.ImageField()
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title
    
    # def save(self, *args, **kwargs):
    # # Only update the updated_on field if the content has actually changed
    #     if self.pk is not None:
    #         orig = Post.objects.get(pk=self.pk)
    #         if orig.content == self.content:
    #             self.updated_on = orig.updated_on
    #     else:
    #         self.updated_on = timezone.now()
            
    #     super(Post, self).save(*args, **kwargs)


    # def save(self, *args, **kwargs):
    #     if self.pk is not None:
    #         orig = Post.objects.get(pk=self.pk)
    #         if orig.content == self.content:
    #             self.updated_at = orig.updated_at
    #     else:
    #         self.updated_at = timezone.now()

    #     super(Post, self).save(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            orig = Post.objects.get(pk=self.pk)
            if orig.content == self.content:
                self.updated_at = orig.updated_at
            else:
                self.updated_at = timezone.now()
        else:
            self.updated_at = timezone.now()

        super(Post, self).save(*args, **kwargs)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

