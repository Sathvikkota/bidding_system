# Generated by Django 4.1.7 on 2023-04-01 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Send_email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
            ],
        ),
        migrations.AlterModelOptions(
            name='placementbid',
            options={'ordering': ['-placementbid_modified']},
        ),
    ]
