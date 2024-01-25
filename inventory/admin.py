from django.contrib import admin
from .models import Product
from django.contrib.auth.models import User,Group
from django.contrib.auth.admin import UserAdmin

admin.site.unregister(User)
admin.site.unregister(Group)

@admin.register(User)
class CustomUserAmin(UserAdmin):
    def get_form(self, request, obj: None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
            form.base_fields['is_superuser'].disabled = True
            form.base_fields['user_permissions'].disabled = True
            form.base_fields['groups'].disabled = True

        return form

#admin.site.register(Product)
# class ReadOnlyAdminMixin:
#     def has_add_permission(self, request):
#         return False

#     def has_change_permission(self, request, obj=None):
#         if request.user.has_perm('inventory.change_product'):
#             return False
#         else:
#             return False

#     def has_delete_permission(self, request, obj=None):
#         return False

#     def has_view_permission(self, request, obj=None):
#         return True

# @admin.register(Product)
# class ProductAdmin(ReadOnlyAdminMixin, admin.ModelAdmin):
#     list_display = ("name", )

#     # def get_form(self, request, obj: None, **kwargs):
#     #     form = super().get_form(request, obj, **kwargs)
#     #     is_superuser = request.user.is_superuser

#     #     if not is_superuser:
#     #         form.base_fields['name'].disabled = True

#     #     return form