# Generated by Django 2.0.2 on 2018-10-20 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_rootserver_source_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddIndex(
            model_name='meeting',
            index=models.Index(fields=['deleted', 'published'], name='api_meeting_deleted_4c15c3_idx'),
        ),
    ]