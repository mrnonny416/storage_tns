# Generated by Django 3.2 on 2022-03-03 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_tns_app', '0015_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='Name_order',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]
