
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',  include('lavagem.urls')),
    path('servico/',  include('servico.urls')),
    path('depoimento/',  include('depoimento.urls')),
    path('equipe/',  include('equipe.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
