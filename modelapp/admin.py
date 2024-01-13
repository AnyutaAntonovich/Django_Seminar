from django.contrib import admin

from .models import User
from django.db.models import F


@admin.action(description='Up age on 10')
def up_age(modeladmin, request, queryset):
    queryset.update(age = 10)


@admin.action(description='Up age on 10(2)')
def up_age2(modeladmin, request, queryset):
    queryset.update(age = F('age') + 10)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    list_filter = ('age',)
    search_fields = ('name', 'surname')
    fieldsets = (('Blog1', {'fields': ('name', 'surname')}), ('Blog2', {'fields': ('bio', 'age')}),)
    actions = (up_age, up_age2,)


admin.site.register(User, UserAdmin)


