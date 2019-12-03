from django.db import models
from django.core import validators

class Item(models.Model):

    SEX_CHOICES = (
        (1, '男性'),
        (2, '女性'),
    )

    name = models.CharField(
        verbose_name='商品名',
        max_length=200,
        blank=True,
        null=True,
    )
    cat = models.CharField(
        verbose_name='カテゴリー',
        max_length=200,
        blank=True,
        null=True,
    )
    sex = models.IntegerField(
        verbose_name='性別',
        choices=SEX_CHOICES,
        default=1
    )
    memo = models.TextField(
        verbose_name='備考',
        max_length=300,
        blank=True,
        null=True,
    )
    link = models.TextField(
        verbose_name='URL',
        max_length=600,
    )
    image = models.TextField(
        verbose_name='画像',
        max_length=300,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        verbose_name='登録日',
        auto_now_add=True
    )
    author = models.CharField(
        verbose_name='投稿者',
        max_length=200,
        blank=True,
        null=True,
    )

    # 以下は管理サイト上の表示設定
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'アイテム'
        verbose_name_plural = 'アイテム'