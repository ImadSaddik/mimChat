# Generated by Django 4.2.2 on 2023-08-12 20:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roomName', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=1000)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chatbot.room')),
            ],
        ),
    ]
