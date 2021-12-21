from django.db import models
from ckeditor.fields import RichTextField

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name="Escritor")
    title = models.CharField(max_length = 55,verbose_name= "Título ")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add = True)
    article_image = models.FileField(null=True,verbose_name="Artículo para mostrar")
    def __str__(self):
        return self.title

    class Meta :
        ordering = ['-created_date']


class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name="Artículo",related_name="comment")
    comment_author = models.CharField(max_length=50,verbose_name="nombre")
    comment_content = models.CharField(max_length=400,verbose_name="Comentario")
    comment_date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.comment_content

    class Meta :
        ordering = ['-comment_date']



