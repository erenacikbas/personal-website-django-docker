# Generated by Django 4.0.3 on 2022-04-26 10:59

from django.db import migrations, models
import django.db.models.deletion
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_remove_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='thumbnail',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.image', verbose_name='Thumbnail'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=sorl.thumbnail.fields.ImageField(upload_to='images/', verbose_name='Image'),
        ),
    ]