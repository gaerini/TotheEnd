# Generated by Django 4.2.1 on 2023-05-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddjapp', '0011_chatting_alter_comment_article_delete_article'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='matched',
            field=models.IntegerField(default=0),
        ),
    ]
