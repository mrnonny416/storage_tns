# Generated by Django 3.2 on 2022-03-03 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_tns_app', '0013_auto_20220301_1610'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='Equipment',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='history',
            name='Brand',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='history',
            name='Category',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
