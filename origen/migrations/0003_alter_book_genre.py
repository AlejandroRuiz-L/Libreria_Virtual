# Generated by Django 5.0.2 on 2024-03-09 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('origen', '0002_author_book_genre_delete_post_book_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(help_text='Seleccione un genero para el libro', to='origen.genre'),
        ),
    ]