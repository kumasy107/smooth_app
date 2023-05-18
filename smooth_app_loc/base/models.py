from django.db import models
from django.utils import timezone

# Create your models here.

About = (("smooth", "SmoothNoteについて"), ("noti", "NotiSaveについて"), ("others", "その他"))

class News(models.Model):
    
    class Meta:
        # テーブル名を定義
        db_table = "news"

    title = models.CharField(verbose_name="タイトル", max_length=255, blank=False, null=False)
    sentence = models.TextField('内容', null=True, blank=False, unique=True) # 追加
    sort=models.IntegerField(verbose_name='ソート',default=0)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
class Question(models.Model):
    class Meta:
        db_table = "question"
    title = models.CharField(verbose_name="質問内容", max_length=255, blank=False, null=False, choices=About, default="smooth")
    sentence = models.TextField('詳細', null=False, blank=False)