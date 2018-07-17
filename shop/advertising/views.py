from django.shortcuts import render

# Create your views here.
def shop_list(request):
    return render(request,'shop_list.html')
