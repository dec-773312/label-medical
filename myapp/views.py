import os
from time import timezone

from django.http import HttpResponse
from .models import User
from django.shortcuts import render, redirect
from .forms import AddForm


# Create your views here.
def index(request):
    # 判断是否为post 方法提交
    if request.method == "GET":
        af = AddForm()
        return render(request, 'Label.html', {'form': af})
        #return render(request, 'index.html', {'select_form': select_form})
    elif request.method == "POST":
        af = AddForm(request.POST, request.FILES)
        # 判断表单值是否和法
        if af.is_valid():
            headimg = af.cleaned_data.get('headimg')
            label = af.cleaned_data.get('label')
            diag = af.cleaned_data.get('diag')
            user = User.objects.create(headimg=headimg, label=label, diag=diag)
            user.save()
            return HttpResponse("%s,%s,%s"%(headimg, label, diag))
    else:
        af = AddForm()
        return render(request, 'Label.html', context={"af": af})
