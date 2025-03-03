# Generated by Django 5.1.5 on 2025-02-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='email',
            field=models.TextField(default='change me', max_length=100, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default='change me', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
    ]
