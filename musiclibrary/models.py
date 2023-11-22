from django.db import models
from django.contrib.auth import get_user_model
from django.shortcuts import reverse
User = get_user_model()


class ArtistModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.RESTRICT, related_name='artist')
    nickname = models.CharField(max_length=20, blank=True, null=False,
                                help_text='Your artist name '
                                          'that will be attached to your content.'
                                          'If not passed, full name will be'
                                          ' considered instead.')

    def __str__(self):
        return self.nickname

    def get_absolute_url(self):
        return reverse('artist_detail', kwargs={'id': self.id})
    class Meta:
        verbose_name = 'artist'
        verbose_name_plural = 'artists'


class AlbumModel(models.Model):

    def path_album_cover(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return 'artists/{0}/albums/{1}/cover/{2}'.format(instance.artist.nickname.replace(' ', ''),
                                                         instance.title.replace(' ', ''), filename)

    title = models.CharField(max_length=100, blank=False, null=False)
    cover = models.ImageField(upload_to=path_album_cover, max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    artist = models.ForeignKey(ArtistModel, blank=True, null=True,
                               on_delete=models.SET_NULL,
                               related_name='albums_by_artist')

    def get_absolute_url(self):
        return reverse('album_detail', kwargs={'id': self.id})

    def __str__(self):
        return f'album:{self.title}'

    class Meta:
        verbose_name = 'album'
        verbose_name_plural = 'albums'


class SongModel(models.Model):
    def path_song_file(instance, filename):
        return f"artists/{instance.album.artist.nickname.replace(' ', '')}\
                                                    /albums/{instance.album.title.replace(' ', '')}\
                                                                        /songs/{instance.title.replace(' ', '')}/{filename}"

    def path_song_cover(instance, filename):
        return f"artists/{instance.album.artist.nickname.replace(' ', '')}\
                                                /albums/{instance.album.title.replace(' ', '')}\
                                                            /songs/{instance.title.replace(' ', '')}/cover/{filename}"

    title = models.CharField(max_length=200, blank=False, null=False)
    lyrics = models.TextField(blank=True, null=True)
    cover = models.ImageField(null=True, max_length=500, blank=True, upload_to=path_song_cover)
    video_url = models.URLField(null=True, blank=True)
    file = models.FileField(upload_to=path_song_file, max_length=5000, blank=False, null=False)
    album = models.ForeignKey(AlbumModel, blank=True, null=True, on_delete=models.SET_NULL,
                              related_name='songs_in_album')
    artists = models.ManyToManyField(ArtistModel, related_name='songs_by_artist')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'song:{self.title}'

    def get_absolute_url(self):
        return reverse('song_detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'song'
        verbose_name_plural = 'songs'


class PlaylistModel(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)
    description = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    uploaded_at = models.DateTimeField(auto_now=True)
    songs = models.ManyToManyField(SongModel, related_name='playlists_of_song')
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False,
                             related_name='playlists_of_user')

    def __str__(self):
        return f'playlist:{self.title}'

    def get_absolute_url(self):
        return reverse('playlist_detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'playlist'
        verbose_name_plural = 'playlists'


class LikedContentModel(models.Model):
    songs = models.ManyToManyField(SongModel, related_name='liked_songs', blank=True,
                                   )
    albums = models.ManyToManyField(AlbumModel, related_name='liked_albums', blank=True,
                                    )
    playlists = models.ManyToManyField(PlaylistModel, related_name='liked_playlists',
                                       blank=True, )
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False, null=False,
                                related_name='liked_content')

    def __str__(self):
        return f'liked by {self.user}'

    def get_absolute_url(self):
        return reverse('liked_detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'liked content'
        verbose_name_plural = 'liked contents'


class FollowModel(models.Model):
    artists = models.ManyToManyField(ArtistModel, related_name='followers_of_artist')
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=False,
                                null=False, related_name='followings_of_user')

    def __str__(self):
        return f'followed by {self.user}'

    def get_absolute_url(self):
        return reverse('follow_detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'following'
        verbose_name_plural = 'followings'
