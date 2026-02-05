from django.contrib import admin
from . models import Service, Master, Gallery, Review, ServiceType, SocialMedia


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ["id"]
    list_editable = ["title",]
    search_fields = ("title",)
    fieldsets = (
        ("Подробная информация", {
            "fields": ("title",)
        }),
        ("Все услуги", {
            "fields": ("types",),
            "classes": ("collapse",)
        })
    )


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "position", "experience")
    list_display_links = ["id", "name"]
    list_editable = ["position", "experience"]
    list_filter = ("position", "experience", "services")
    ordering = ("position", "experience")
    fieldsets = (
        ("Основное", {
            "fields": ("name", "position", "experience", "photo")
        }),
        ("Дополнительное", {
            "fields": ("services", "description", "media", "link"),
            "classes": ("collapse",)
        })
    )


@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "service")
    list_display_links = ["id",]
    list_editable = ["title", "service"]
    fieldsets = (
        ("Подробная информация", {
            "fields": ("title", "service", "image")
        }),
    )


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "master", "rating")
    list_editable = ["master", "rating"]
    list_display_links = ["id",]
    ordering = ("rating", "created_at")
    readonly_fields = ("created_at",)
    fieldsets = (
        ("Основное", {
            "fields": ("master", "rating")
        }),
        ("Отзывы", {
            "fields": ("comment", "created_at"),
            "classes": ("collapse",)
        })
    )


@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price")
    list_display_links = ["id",]
    list_editable = ["title", "price"]
    ordering = ["id", "-price"]
    fieldsets = (
        ("Основная", {
            "fields": ("title", "price")
        }),
    )


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ["id", "name"]
    fieldsets = (
        ("Сеть", {
            "fields": ("name",)
        }),
    )