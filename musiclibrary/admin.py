from django.contrib import admin
from .models import ArtistModel, AlbumModel, SongModel,  LikedContentModel, \
    FollowModel

admin.site.register(ArtistModel)
admin.site.register(AlbumModel)
admin.site.register(SongModel)
admin.site.register(LikedContentModel)
admin.site.register(FollowModel)

