# Generated by Django 4.2.1 on 2023-05-23 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apartment', '0006_alter_apartmentmodel_img_alter_apartmentmodel_text'),
        ('home', '0006_usersmodel_alter_booknow_comnat'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UsersModel',
        ),
        migrations.AlterField(
            model_name='booknow',
            name='comnat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='apartment.apartmentmodel', verbose_name='apartments'),
        ),
    ]
