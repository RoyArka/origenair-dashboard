# Generated by Django 3.0.7 on 2020-07-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0029_auto_20200703_0219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='org_avatar',
            field=models.ImageField(blank=True, default='../origen/static/img/placeholder.jpg/', null=True, upload_to='org'),
        ),
    ]