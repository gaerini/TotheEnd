# Generated by Django 4.2.1 on 2023-05-20 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ddjapp', '0004_rename_title_room_talk_topic_rename_leader_room_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='request_member',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('req_member', models.IntegerField()),
                ('reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Request', to='ddjapp.room')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='room2', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
