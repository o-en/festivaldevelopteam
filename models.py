from django.db import models

# Create your models here.
class Board(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

class Comment(models.Model):
    CHOICE_BUSY = (
        ('매우 혼잡','매우 혼잡'),('혼잡', '혼잡'),('보통', '보통'),('여유', '여유'),
    )
    post = models.ForeignKey(Board, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)
    comment_contents = models.CharField(max_length=400)
    dropdown = models.CharField(max_length=10)
    busy = models.CharField(max_length=20, choices = CHOICE_BUSY)
    password =models.CharField(max_length=20, null=False)

    class Meta:
        ordering = ['-comment_date']

    def approve(self):
        self.approved_comment = True
        self.save() 

    def __str__(self):
        return self.text