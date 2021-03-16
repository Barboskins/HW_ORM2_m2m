from django.db import models


class Article(models.Model):

    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=10, verbose_name='Название тега')
    article = models.ManyToManyField(Article, through='ArtickeTag', verbose_name='Название статьи', related_name='tag')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'

    def __str__(self):
        return self.title

class ArtickeTag(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Тег')
    article = models.ForeignKey(Article, on_delete=models.CASCADE, verbose_name='Статья')
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.article}-{self.tag}'

