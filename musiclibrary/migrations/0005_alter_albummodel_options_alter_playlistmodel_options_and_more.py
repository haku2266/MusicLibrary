# Generated by Django 4.2.7 on 2023-11-26 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musiclibrary', '0004_alter_likedcontentmodel_albums_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='albummodel',
            options={'ordering': ['-uploaded_at'], 'verbose_name': 'album', 'verbose_name_plural': 'albums'},
        ),
        migrations.AlterModelOptions(
            name='playlistmodel',
            options={'ordering': ['-uploaded_at'], 'verbose_name': 'playlist', 'verbose_name_plural': 'playlists'},
        ),
        migrations.AlterField(
            model_name='likedcontentmodel',
            name='albums',
            field=models.ManyToManyField(blank=True, related_name='liked_albums', to='musiclibrary.albummodel'),
        ),
        migrations.AlterField(
            model_name='likedcontentmodel',
            name='playlists',
            field=models.ManyToManyField(blank=True, related_name='liked_playlists', to='musiclibrary.playlistmodel'),
        ),
        migrations.AlterField(
            model_name='likedcontentmodel',
            name='songs',
            field=models.ManyToManyField(blank=True, related_name='liked_songs', to='musiclibrary.songmodel'),
        ),
    ]
