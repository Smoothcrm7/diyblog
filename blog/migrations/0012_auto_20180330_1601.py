# Generated by Django 2.0.3 on 2018-03-30 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180326_1157'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='blog_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='blog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='blog.Blog'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comments',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
