# from rest_framework import permissions
#
# from .models import Permission
#
#
# class AppsApiPermission(permissions.BasePermission):
#     def has_permission(self, request, view):
#         if view.action == 'list':
#             return request.user.has_module_perms(Permission.perm_list_app_name) or request.user.has_module_perms(
#                 Permission.perm_list_comp_app_name)
#         elif view.action == 'create':
#             return request.user.has_module_perms(Permission.perm_add_app_name)
#         elif view.action == "retrieve":
#             return request.user.has_module_perms(Permission.perm_list_app_name)
#         elif view.action in ['update', 'partial_update', 'destroy']:
#             return request.user.has_module_perms(Permission.perm_edit_app_name)
#         else:
#             return False
#
#     def has_object_permission(self, request, view, obj):
#         if view.action == 'list':
#             return request.user.has_module_perms(Permission.perm_list_app_name) or request.user.has_module_perms(
#                 Permission.perm_list_comp_app_name)
#         elif view.action == 'create':
#             return request.user.has_module_perms(Permission.perm_add_app_name)
#         elif view.action == "retrieve":
#             return request.user.has_module_perms(Permission.perm_list_app_name)
#         elif view.action in ['update', 'partial_update', 'destroy']:
#             return request.user.has_module_perms(Permission.perm_edit_app_name)
#         else:
#             return False
