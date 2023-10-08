# Generated by Django 4.2.6 on 2023-10-08 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=50)),
                ('auth_type', models.CharField(choices=[('Application', 'Application'), ('Bearer', 'Bearer')], max_length=12)),
                ('application_token', models.CharField(max_length=50, null=True)),
                ('refresh_token', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
