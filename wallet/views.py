from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render,render_to_response
# Create your views here.
from django.core import serializers
from .models import article,ann

from itertools import chain
#产品介绍
def cpjs(request):
    return render_to_response("cpjs.html")
#贷款保障
def dkbz(request):
    return render_to_response('dkbz.html')
#门店地址

def mddz(request):
    return render_to_response('mddz.html')
# 企业文化
def qywh(request):
    return render_to_response('qywh.html')

#首页下部文章1
def articleOne(request):
    return render_to_response('homeEasy.html')
#首页下部文章2
def articleTwo(request):
    return render_to_response('homeLoan.html')



#首页json数据 model=wallet.article=2篇链接  wallet.ann=公告.
def jsonHome(request):

    linkurl = article.objects.all()
    announcement = ann.objects.all()
    result_list = list(chain(linkurl,announcement))

    json_data = serializers.serialize("json",result_list)
    return HttpResponse(json_data,content_type="application/json")
