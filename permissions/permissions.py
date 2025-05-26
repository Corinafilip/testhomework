from rest_framework.permissions import BasePermission

class CanGetTasksPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('greetings.can_get_tasks')

class CanGetSubTasksPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('greetings.can_get_subtasks')

