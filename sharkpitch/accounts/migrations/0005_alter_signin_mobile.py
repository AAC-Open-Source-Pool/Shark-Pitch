# Generated by Django 5.1 on 2024-11-21 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_signin_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='mobile',
            field=models.BigIntegerField(default=None),
        ),
    ]