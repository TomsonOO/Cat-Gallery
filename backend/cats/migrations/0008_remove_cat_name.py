# Generated by Django 4.0.3 on 2022-03-30 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0007_alter_cat_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cat',
            name='name',
        ),
    ]
