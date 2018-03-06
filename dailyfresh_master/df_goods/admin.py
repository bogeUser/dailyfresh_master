#coding: utf-8

"""注册模型类"""
from __future__ import unicode_literals
from django.contrib import admin
from df_goods.models import TypeInfo, GoodsInfo

class TypeInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']

class GoodsInfoAdmin(admin.ModelAdmin):
    list_per_page = 15
    list_display = ['id', 'gtitle', 'gprice', 'gunit', 'gclick', 'gkucun', 'gcontent','gtype']

admin.site.register(TypeInfo, TypeInfoAdmin)
admin.site.register(GoodsInfo, GoodsInfo)

















