from django.contrib import admin
from django.urls import path, include
from article import views as articleViews
from note import views as noteViews
from music import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('articles/', include("article.urls")),
    path('user/', include("user.urls")),
    path('notes/', include("note.urls")),
    path('music/', include("music.urls")),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
