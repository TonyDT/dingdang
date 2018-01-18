from django.db import models


# Create your models here.

#站内公告
class ann(models.Model):
    title = models.CharField('公告',max_length=60)

    def __str__(self):
        return self.title


    class Meta:
        verbose_name ='首页公告'
        verbose_name_plural = verbose_name



# 首页贷款指南  防诈骗贷款提醒
class article(models.Model):
    title = models.CharField('文章标题',max_length=30)
    introduce = models.CharField('内容简介',max_length=100)
    urlDetail = models.CharField('内容详情链接',max_length=500)
    thumbnailImage = models.ImageField('缩略图',upload_to='img/%Y%m%d')

    def __str__(self):
        return  self.title

    class Meta:
        db_table = 'ImageStore'
        verbose_name = '首页文章'
        verbose_name_plural = verbose_name


