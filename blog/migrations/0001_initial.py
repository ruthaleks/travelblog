# Generated by Django 2.0.6 on 2018-06-20 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=50)),
                ('comment_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Comment published')),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=100)),
                ('photo_text', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Photo published')),
                ('travel_date', models.DateTimeField(verbose_name='Photo travel date')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', markdownx.models.MarkdownxField()),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Post published')),
                ('travel_date', models.DateTimeField(verbose_name='Post travel date')),
                ('last_edited', models.DateTimeField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='photo',
            name='post',
            field=models.ManyToManyField(to='blog.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
