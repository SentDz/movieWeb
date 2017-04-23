# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from django.http import HttpResponse

from moviesearch.models import letv, aiqiyi
import urllib

def hello(request):
    context = {}
    context['title'] = "草榴电影网"
    context['keywords'] = "草榴,草榴电影,fuli影城"
    context['description'] = "草榴电影 最干净的免费电影网,给你更方便的高清无广告电影电视剧在线观看,草榴电影电影下载"
    context['headerhelp'] = "欢迎来到草榴电影，我们因为电影而相聚。"
    return render(request, "a.html", context)


def search(request):
    message = ''
    context = {}
    context['movies'] = []
    context['key'] = ""
    request.encoding='utf-8'
    if 'q' in request.GET:
        ida = request.GET['q']
        aa = letv.objects(name__contains=ida)
        bb = aiqiyi.objects(name__contains=ida)
        context['key'] = ida
        for n in aa:
            sss = {}
            sss['title'] = n.name
            urldecode = str(n.vids)
            abs = urldecode.split(',')
            sss['url'] = "http://www.le.com/ptv/vplay/"+abs[0]+".html"
            sss['desc'] = n.description
            sss['auth'] = n.tag
            sss['type'] = n.subCategoryName
            sss['img'] = n.images['90*120']
            context['movies'].append(sss)
        for x in bb:
            sss = {}
            sss['title'] = x.name
            sss['url'] = x.url
            sss['img'] = x.img
            sss['auth'] = ""
            sss['type'] = ""
            sss['desc'] = "描述暂时未抓取"
            context['movies'].append(sss)
    else:
        message = '你提交了空表单'

    return render(request, "result.html", context)



def look(request):
    context = {}
    context['url'] = ""

    if 'url' in request.GET:
        url = request.GET['url']
        context['url'] =  "http://www.vipjiexi.com/tong.php?url="+url

    return render(request,"play.html",context)