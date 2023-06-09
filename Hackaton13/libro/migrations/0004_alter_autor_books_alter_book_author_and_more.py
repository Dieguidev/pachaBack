# Generated by Django 4.2.1 on 2023-06-02 01:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('libro', '0003_alter_autor_books_alter_book_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autor',
            name='books',
            field=models.ManyToManyField(to='libro.book'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='registrolibro',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
