from django.db import models

# カテゴリマスタ
class m_category(models.Model):
    name = models.CharField('カテゴリ', max_length=50)

    def __str__(self):
        return self.name

# タグマスタ
class m_tag(models.Model):
    name = models.CharField('タグ', max_length=50)

    def __str__(self):
        return self.name
    
# テーブル
class t_table(models.Model):
    category = models.ForeignKey(
                m_category, verbose_name='カテゴリ',
                on_delete=models.PROTECT
            )
    tag = models.ManyToManyField(m_tag, verbose_name='タグ', null=True, blank=True)
    title = models.CharField(verbose_name='タイトル', max_length=200)
    content = models.TextField(verbose_name='内容')
    image = models.ImageField(verbose_name = '画像',upload_to = 'images/')
    newadddate = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updatedate = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    deletedate = models.DateTimeField(verbose_name='削除日時', null=True, blank=True)
    views = models.PositiveIntegerField(verbose_name='閲覧数', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-newadddate',) 