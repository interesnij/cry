# Generated by Django 2.2.12 on 2020-05-27 21:56

from django.conf import settings
import django.contrib.postgres.indexes
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields
import users.helpers
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog_categories', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False, unique=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='uuid')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание курса')),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to=users.helpers.upload_to_user_directory)),
                ('video', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ссылка на вводный видео-ролик')),
                ('is_active', models.BooleanField(default=False, verbose_name='Курс активен')),
                ('is_deleted', models.BooleanField(default=False, verbose_name='Курс удален')),
                ('is_private', models.BooleanField(default=False, verbose_name='Курс приватный')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Время публикации')),
                ('is_reklama', models.BooleanField(default=False, verbose_name='Это реклама')),
                ('votes_off', models.BooleanField(default=False, verbose_name='Лайки-дизлайки отключены')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_categories.BlogCategory', verbose_name='Категория')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'посты',
                'verbose_name': 'пост',
            },
        ),
        migrations.CreateModel(
            name='BlogFavourites',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Blog', verbose_name='Пост')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blog_favorites', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name_plural': 'Избранные Посты',
                'verbose_name': 'Избранный Пост',
            },
        ),
        migrations.AddIndex(
            model_name='blogfavourites',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='blog_blogfa_created_ac2e60_brin'),
        ),
        migrations.AlterUniqueTogether(
            name='blogfavourites',
            unique_together={('course', 'user')},
        ),
        migrations.AddIndex(
            model_name='blog',
            index=django.contrib.postgres.indexes.BrinIndex(fields=['created'], name='blog_blog_created_a423be_brin'),
        ),
    ]