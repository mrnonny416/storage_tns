# Generated by Django 3.2 on 2022-03-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage_tns_app', '0020_storage_masterkey'),
    ]

    operations = [
        migrations.CreateModel(
            name='equipment',
            fields=[
                ('order', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Masterkey', models.CharField(blank=True, max_length=50)),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Brand', models.CharField(blank=True, max_length=50)),
                ('Type', models.CharField(blank=True, max_length=50)),
                ('Category', models.CharField(blank=True, max_length=50)),
                ('Amount', models.IntegerField()),
                ('Picture', models.ImageField(blank=True, upload_to='storage')),
            ],
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('order', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('Masterkey', models.CharField(blank=True, max_length=50)),
                ('Name', models.CharField(blank=True, max_length=50)),
                ('Brand', models.CharField(blank=True, max_length=50)),
                ('Type', models.CharField(blank=True, max_length=50)),
                ('Category', models.CharField(blank=True, max_length=50)),
                ('Amount', models.IntegerField()),
                ('Picture', models.ImageField(blank=True, upload_to='storage')),
            ],
        ),
    ]
