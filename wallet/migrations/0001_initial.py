# Generated by Django 2.0.1 on 2018-01-18 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ann',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, verbose_name='公告')),
            ],
        ),
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, verbose_name='文章标题')),
                ('introduce', models.CharField(max_length=100, verbose_name='内容简介')),
                ('urlDetail', models.CharField(max_length=500, verbose_name='内容详情链接')),
                ('thumbnailImage', models.ImageField(upload_to='img/%Y%m%d', verbose_name='缩略图')),
            ],
            options={
                'verbose_name': '首页文章',
                'verbose_name_plural': '首页文章',
                'db_table': 'ImageStore',
            },
        ),
    ]