# Generated by Django 3.2 on 2022-02-23 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_tns_app', '0004_auto_20220223_1138'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='Mataterial',
            new_name='Material',
        ),
        migrations.AlterField(
            model_name='equipment',
            name='Picture',
            field=models.CharField(blank=True, max_length=4000000),
        ),
    ]
