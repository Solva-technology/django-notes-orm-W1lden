from django.contrib import admin

from .models import Category, Note, Status, User, UserProfile


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("title", "description")
    search_fields = ("title",)
    list_filter = ("title",)
    ordering = ("title",)


class NoteAdmin(admin.ModelAdmin):
    list_display = ("author", "created_at", "display_categories")
    search_fields = ("categories",)
    list_filter = ("created_at",)
    ordering = ("-created_at",)

    def display_categories(self, obj):
        return ", ".join([c.title for c in obj.categories.all()])

    display_categories.short_description = "Categories"


class StatusAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    list_filter = ("name",)
    ordering = ("name",)


class UserAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("email",)
    list_filter = ("name",)
    ordering = ("name",)


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user",)
    search_fields = ("user",)
    list_filter = ("user",)
    ordering = ("user",)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Note, NoteAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
