# Generated by Django 5.1 on 2024-11-21 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_alter_signin_mobile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signin',
            name='mobile',
        ),
        migrations.AddField(
            model_name='signin',
            name='mobile_num',
            field=models.CharField(default=None, unique=True),
        ),
    ]