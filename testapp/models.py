from django.db import models
from django.urls import reverse

class Result(models.Model):
    name = models.CharField(max_length=50,verbose_name='氏名')
    language = models.PositiveIntegerField(verbose_name='国語')
    math = models.PositiveIntegerField(verbose_name='数学')
    english = models.PositiveIntegerField(verbose_name='英語')


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('testapp:detail',kwargs={'pk':self.pk})