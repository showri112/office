# Generated by Django 3.2 on 2022-10-28 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='officemodel',
            name='Address',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='officemodel',
            name='Photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
