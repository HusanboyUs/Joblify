# Generated by Django 4.1 on 2022-08-09 16:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_jobs_options_jobs_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobs',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]