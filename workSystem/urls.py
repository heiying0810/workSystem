from django.contrib import admin
from django.urls import path
import works.views

urlpatterns = [
    path('', admin.site.urls),
]
handler404 = works.views.page_not_found