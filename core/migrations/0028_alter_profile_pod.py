# Generated by Django 4.2.1 on 2023-06-02 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_alter_profile_pod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='pod',
            field=models.CharField(default='', max_length=50),
        ),
    ]
