# Generated by Django 4.1.7 on 2023-04-01 11:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_send_feedback'),
    ]

    operations = [
        migrations.RenameField(
            model_name='send_email',
            old_name='email',
            new_name='email1',
        ),
    ]
