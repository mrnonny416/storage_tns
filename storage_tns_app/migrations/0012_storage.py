# Generated by Django 3.2 on 2022-03-01 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_tns_app', '0011_auto_20220301_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='storage',
            fields=[
                ('order', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Material', models.CharField(max_length=50)),
                ('Type', models.CharField(blank=True, max_length=50)),
                ('Category', models.CharField(blank=True, max_length=50)),
                ('Amount', models.IntegerField()),
                ('Picture', models.ImageField(blank=True, upload_to='material')),
            ],
        ),
    ]
