# Generated by Django 4.2.7 on 2023-11-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclibrary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createpostmodel',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]