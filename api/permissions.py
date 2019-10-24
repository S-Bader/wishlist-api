from rest_framework.permissions import BasePermission

class IsStaffOrOwner(BasePermission):
	message = 'You cannot view this item, sucks to be you, I guess :/ ' 

	def has_object_permission(self, request, view, obj):
		if request.user.is_staff or (obj.added_by == request.user):
			return True
		return False