from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .produto.views import ProdutoList, ProdutoListCreate, ProdutoDelete
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProdutoList.as_view()),
    path('products', ProdutoListCreate.as_view()),
    path('products/<int:pk>', ProdutoDelete.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
