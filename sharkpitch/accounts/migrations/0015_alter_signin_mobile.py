# Generated by Django 5.1 on 2024-11-25 16:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_rename_mobile_num_signin_mobile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signin',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
