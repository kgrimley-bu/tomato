# Generated by Django 2.0.2 on 2018-04-05 03:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rootserver_last_successful_import'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicebody',
            name='helpline',
            field=models.CharField(max_length=255, null=True),
        ),
    ]