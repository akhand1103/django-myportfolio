# Generated by Django 4.2.1 on 2023-05-16 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='desc',
            new_name='description',
        ),
    ]
