# Generated by Django 5.1.3 on 2024-11-22 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.TextField()),
                ('member_id', models.TextField()),
                ('join_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Member_informaiton',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.TextField()),
                ('birth', models.DateTimeField()),
            ],
        ),
    ]
