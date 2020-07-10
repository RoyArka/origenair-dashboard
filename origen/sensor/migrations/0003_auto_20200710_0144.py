# Generated by Django 3.0.6 on 2020-07-10 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0033_merge_20200703_1654'),
        ('sensor', '0002_auto_20200708_2329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sensor',
            name='organization',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sensors', to='organization.Organization'),
        ),
    ]
