# Generated by Django 4.2.1 on 2023-05-23 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0005_comment_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='apartmentmodel',
            name='img',
            field=models.ImageField(null=True, upload_to='media/'),
        ),
        migrations.AlterField(
            model_name='apartmentmodel',
            name='text',
            field=models.TextField(null=True),
        ),
    ]
