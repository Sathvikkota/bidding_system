# Generated by Django 4.1.7 on 2023-04-01 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_send_email_alter_placementbid_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
    ]
