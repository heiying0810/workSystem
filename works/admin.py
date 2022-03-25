from django.contrib import admin

admin.site.site_header = '自助工单系统'
admin.site.site_title = '工单系统'

from .models import Worklist,Jiazhikehu
@admin.register(Worklist)
class ApplistAdmin(admin.ModelAdmin):
    search_fields = ['kehuName']
    list_display = ('id','created_time','name','kehuName','type','phone','numRmb','lir','name_status','text')
    list_per_page = 15
    ordering = ('-created_time',)
    list_display_links = ('kehuName',)


@admin.register(Jiazhikehu)
class ApplistAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('id','name','phone','type','text','created_time')
    list_per_page = 15
    ordering = ('-created_time',)
    list_display_links = ('name',)
