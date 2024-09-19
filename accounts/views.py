from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    template_name = 'accounts/login.html'
    return render(request, template_name)

def register_view(request):
    # 회원가입 폼을 처리하는 로직
    template_name = 'accounts/register.html'
    return render(request, template_name)