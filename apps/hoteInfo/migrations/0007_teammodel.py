# Generated by Django 4.2.1 on 2023-05-20 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hoteInfo', '0006_alter_menu_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/')),
                ('name', models.CharField(max_length=50)),
                ('bio', models.TextField(max_length=150)),
            ],
        ),
    ]