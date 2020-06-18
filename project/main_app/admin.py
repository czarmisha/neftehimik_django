from django import forms
from django.contrib import admin
from django.utils.safestring import mark_safe
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from main_app.models import Category, News, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent', 'get_image')
    search_fields = ('name',)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'Изображение'


class NewsAdminForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = News
        fields = '__all__'


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pub_date', 'get_image')
    list_display_links = ('id', 'title')
    save_as = True
    save_on_top = True
    search_fields = ('title',)
    readonly_fields = ('get_image', 'pub_date')
    form = NewsAdminForm

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'Изображение'


class ProductAdminForm(forms.ModelForm):
    options = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Product
        fields = '__all__'


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sub_category', 'get_image')
    list_display_links = ('id', 'name')
    save_as = True
    save_on_top = True
    search_fields = ('name', 'sub_category',)
    list_filter = ('sub_category',)
    form = ProductAdminForm

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50">')
        return '-'

    get_image.short_description = 'Изображение'


admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Product, ProductAdmin)
