# Generated by Django 3.1.4 on 2020-12-24 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workouts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workout_name', models.CharField(default='', max_length=40)),
                ('workout_type', models.CharField(choices=[('FT', 'For Time'), ('AMRAP', 'As Many Rounds As Possible'), ('MW', 'Max. Weight')], max_length=5)),
                ('workout_category', models.CharField(choices=[('PL', 'Power Lifts'), ('OL', 'Olympic Lifts'), ('SP', 'Speed'), ('EN', 'Endurance'), ('BW', 'Body Weight'), ('HE', 'Heavy'), ('LI', 'Light'), ('LO', 'Long')], max_length=5)),
                ('description', models.TextField()),
            ],
        ),
    ]
