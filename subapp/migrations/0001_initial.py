# Generated by Django 5.0.6 on 2024-06-07 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='POST_MODEL',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('body', models.CharField(blank=True, max_length=200, null=True, verbose_name='Body')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created DataTime')),
            ],
        ),
    ]
