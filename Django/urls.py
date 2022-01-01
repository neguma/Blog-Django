from django.contrib import admin
from django.urls import path, include
from article.views import *
from note.views import *
from music.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('detail/<int:id>', detail, name="detail"),
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),
    path('notes/', include("note.urls")),
    path('music/', include("music.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
