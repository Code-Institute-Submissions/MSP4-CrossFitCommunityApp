# Generated by Django 3.1.4 on 2020-12-30 20:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0013_auto_20201230_1206'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=250)),
                ('log_id', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='workouts.log')),
                ('member', models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]