from django.shortcuts import redirect

# =====Authencation=======
def auth(view_fun):
    def wrapped_view(request,*args, **kwargs):
        if request.user.is_authenticated==False:
            return redirect('login')
        return view_fun(request,*args, **kwargs)
    return wrapped_view

# =====Authencation=======
def guest(view_fun):
    def wrapped_view(request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashbord')
        return view_fun(request,*args, **kwargs)
    return wrapped_view