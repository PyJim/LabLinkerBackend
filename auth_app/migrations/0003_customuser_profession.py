# Generated by Django 5.1.3 on 2025-03-06 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_customuser_avatar_alter_customuser_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profession',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
