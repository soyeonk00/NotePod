# Generated by Django 4.2.1 on 2023-05-23 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0023_rename_podname_pod_pod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pod',
            old_name='pod',
            new_name='name',
        ),
        migrations.AddField(
            model_name='pod',
            name='district',
            field=models.CharField(default='', max_length=10),
        ),
    ]
