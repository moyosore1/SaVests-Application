from django.shortcuts import redirect
from django.http import HttpResponse


def check_if_is_staff(view_func):
	def wrapper_func(request, *args, **kwargs):
		if request.user.is_staff:
			return view_func(request, *args, **kwargs)
		else:
			return HttpResponse("You are not authorized to view this page")

	return wrapper_func
			