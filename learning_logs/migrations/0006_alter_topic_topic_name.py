# Generated by Django 4.0.4 on 2022-06-13 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0005_alter_topic_topic_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='topic_name',
            field=models.CharField(max_length=60),
        ),
    ]
