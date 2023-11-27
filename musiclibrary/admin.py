from django.contrib import admin
from .models import *

admin.site.register(SongModel)
admin.site.register(ArtistModel)
admin.site.register(AlbumModel)
admin.site.register(FollowModel)
admin.site.register(LikedContentModel)