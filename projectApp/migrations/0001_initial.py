# Generated by Django 3.1.4 on 2020-12-25 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project/')),
                ('title', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200, null=True)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
