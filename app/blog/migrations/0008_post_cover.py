# Generated by Django 4.0.3 on 2022-04-26 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_postcomment_options_alter_postmeta_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='blog/', verbose_name='Cover Image'),
        ),
    ]
