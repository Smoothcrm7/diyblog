# Generated by Django 2.0.3 on 2018-03-18 03:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_profile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-post_date']},
        ),
    ]
