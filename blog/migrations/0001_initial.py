# Generated by Django 3.2.9 on 2021-11-28 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=30)),
                ('text', models.TextField(default='')),
                ('author', models.CharField(default='', max_length=30)),
                ('created_at', models.DateField(auto_now=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
