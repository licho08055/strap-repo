# Generated by Django 3.2 on 2022-08-08 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strapi_app', '0003_auto_20220807_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='character',
            name='people',
        ),
        migrations.RemoveField(
            model_name='people',
            name='friends_id',
        ),
        migrations.RemoveField(
            model_name='people',
            name='user_id',
        ),
        migrations.AddField(
            model_name='character',
            name='type_people',
            field=models.ManyToManyField(related_name='type_people', to='strapi_app.People'),
        ),
        migrations.AddField(
            model_name='people',
            name='types',
            field=models.CharField(default='solomon', max_length=100),
        ),
    ]