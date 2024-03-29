from django.urls import path
from .views import file_upload, search_results, submit,view_docx,view_graph
from django.conf import settings
from django.conf.urls.static import static

app_name = 'file_upload_app'

urlpatterns = [
    path('main/', file_upload, name='file_upload'),
    path('search/',search_results, name='search_results'),
    path('submit/',submit,name='submit'),
    path('viewdocx/', view_docx, name='view_docx'),
    path('view_graph/', view_graph, name='view_graph'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)