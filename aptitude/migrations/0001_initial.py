# Generated by Django 4.1.3 on 2023-02-19 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LCMHCF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques', models.CharField(default='true', max_length=500)),
                ('Op1', models.CharField(default='true', max_length=100)),
                ('Op2', models.CharField(default='true', max_length=100)),
                ('Op3', models.CharField(default='true', max_length=100)),
                ('Op4', models.CharField(default='true', max_length=100)),
                ('Corans', models.CharField(default='true', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='RatioP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques1', models.CharField(default='true', max_length=500)),
                ('Op11', models.CharField(default='true', max_length=100)),
                ('Op12', models.CharField(default='true', max_length=100)),
                ('Op13', models.CharField(default='true', max_length=100)),
                ('Op14', models.CharField(default='true', max_length=100)),
                ('Corans1', models.CharField(default='true', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SICI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(default='true', max_length=500)),
                ('Option1', models.CharField(default='true', max_length=100)),
                ('Option2', models.CharField(default='true', max_length=100)),
                ('Option3', models.CharField(default='true', max_length=100)),
                ('Option4', models.CharField(default='true', max_length=100)),
                ('Corrans', models.CharField(default='true', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Simplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques3', models.CharField(default='true', max_length=500)),
                ('Op31', models.CharField(default='true', max_length=100)),
                ('Op32', models.CharField(default='true', max_length=100)),
                ('Op33', models.CharField(default='true', max_length=100)),
                ('Op34', models.CharField(default='true', max_length=100)),
                ('Corans3', models.CharField(default='true', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TimeW',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Ques2', models.CharField(default='true', max_length=500)),
                ('Op21', models.CharField(default='true', max_length=100)),
                ('Op22', models.CharField(default='true', max_length=100)),
                ('Op23', models.CharField(default='true', max_length=100)),
                ('Op24', models.CharField(default='true', max_length=100)),
                ('Corans2', models.CharField(default='true', max_length=100)),
            ],
        ),
    ]
