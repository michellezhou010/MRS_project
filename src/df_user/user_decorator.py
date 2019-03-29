from django.http import HttpResponseRedirect
# to login page
def login(func):
    def login_fun(request, *args, **kwargs):
        if request.session.has_key('user_id'):      #if userid in session
            return func(request, *args, **kwargs)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url',request.get_full_path())   #path to current cookie --> url
            return red
    return login_fun

'''
http://127.0.0.1:8000/200/?type=10
request.path: current path ,/200/
request,get_full_path(): full path, /200/?type=10
'''