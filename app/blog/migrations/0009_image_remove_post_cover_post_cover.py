# Generated by Django 4.0.3 on 2022-04-26 10:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_cover'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, verbose_name='Image Name')),
                ('image', models.ImageField(upload_to='images/', verbose_name='Image')),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updatedAt', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='cover',
        ),
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ManyToManyField(blank=True, to='blog.image', verbose_name='Cover'),
        ),
    ]
