# Generated by Django 4.0.5 on 2022-06-16 08:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('spm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='some',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]