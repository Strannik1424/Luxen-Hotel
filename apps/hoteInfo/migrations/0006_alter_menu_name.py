# Generated by Django 4.2.1 on 2023-05-15 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteInfo', '0005_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
