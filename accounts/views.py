from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    template_name = 'accounts/login.html'
    return render(request, template_name)

def register(request):
    # 회원가입 폼을 처리하는 로직
    return render(request, 'accounts/register.html')