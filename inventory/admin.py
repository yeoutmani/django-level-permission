from django.contrib import admin
from .models import Product
from guardian.admin import GuardedModelAdmin

@admin.register(Product)
class ProductAdmin(GuardedModelAdmin):
    list_display = ('name', )

    def has_module_permission(self, request) :
        if super().has_module_permission(request):
            return True

    def get_queryset(self, request):
        return super().get_queryset(request)

    def has_permission(sefl, request, obj, action):
        opts = sefl.opts
        code_name = f'{action}_{opts.model_name}'
        if obj:
            return request.user.has_perm(f'{opts.app_label}.{code_name}', obj)
        else:
            return True

    def has_view_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'view')
    
    def has_delete_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'delete')
    
    def has_change_permission(self, request, obj=None):
        return self.has_permission(request, obj, 'change')
