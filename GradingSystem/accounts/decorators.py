from django.http import HttpResponse
from django.shortcuts import redirect

def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('smislogin')
        else:
            return view_func(request, *args, **kwargs)

    return wrapper_func

#Allowed_Users    
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name

            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return redirect('smishome')

        return wrapper_func
    return decorator

#Admin_Only
def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        if group == 'student':
            return redirect('smishome')

        if group == 'admin':
            return view_func(request, *args, **kwargs)

    return wrapper_func
