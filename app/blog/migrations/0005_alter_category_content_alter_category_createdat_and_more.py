# Generated by Django 4.0.3 on 2022-04-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_alter_post_createdat_alter_post_updatedat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='content',
            field=models.TextField(max_length=200, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='category',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='category',
            name='metaTitle',
            field=models.CharField(blank=True, max_length=100, verbose_name='Meta Title'),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='post',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at'),
        ),
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(blank=True, max_length=250, verbose_name='Summary'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated at'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='content',
            field=models.TextField(max_length=500, verbose_name='Content'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created At'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='title',
            field=models.TextField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='updatedAt',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated At'),
        ),
        migrations.AlterField(
            model_name='postmeta',
            name='metaKey',
            field=models.CharField(max_length=100, verbose_name='Meta Key'),
        ),
        migrations.AlterField(
            model_name='postmeta',
            name='metaValue',
            field=models.TextField(blank=True, max_length=250, verbose_name='Meta Value'),
        ),
    ]