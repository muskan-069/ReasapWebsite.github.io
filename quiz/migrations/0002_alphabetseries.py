# Generated by Django 4.1.3 on 2023-02-19 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='alphabetseries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques', models.CharField(default='true', max_length=500)),
                ('Opt1', models.CharField(default='true', max_length=100)),
                ('Op2', models.CharField(default='true', max_length=100)),
                ('Op3', models.CharField(default='true', max_length=100)),
                ('Op4', models.CharField(default='true', max_length=100)),
                ('Corans', models.CharField(default='true', max_length=100)),
            ],
        ),
    ]
