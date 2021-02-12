from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .produto.views import ProdutoList, ProdutoListCreate, ProdutoDelete
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ProdutoList.as_view()),
    path('products', ProdutoListCreate.as_view()),
    path('products/<int:pk>', ProdutoDelete.as_view()),

    # Path to API Schema
    path('openapi/', get_schema_view(
        title='Product Schema',
        description='API developers hoping to use our schema'), name='openapi-schema'),

    # Path to API Documentation
    path('docs/', TemplateView.as_view(
        template_name='documentation.html',
        extra_context={'schema_url':'openapi-schema'}), name='swagger-ui'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
