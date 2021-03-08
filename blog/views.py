from django.http import HttpResponse
from django.shortcuts import render
from .models import *
import math
# Create your views here.
from django.views import View

# Django分页
from django.core.paginator import Paginator



class IndexeView(View):
    def get(self,request):
        return HttpResponse("hello")


# 渲染主页面
def queryAll(request, num=2):

    # request.GET.get('num', 1) 获取get请求里面的num字段，获取不到就设置为1
    # num = request.GET.get('num', 1)  # 字符串形式
    num = int(num)
    post_list = Post.objects.all().order_by('-created')
    # 创建分液器对象
    # 数据，分页数量
    page_obj = Paginator(post_list, per_page=1)
    # 获取当前页的数据
    perPageList = page_obj.page(num)

    # 生成页表数的列表
    begin = (num - int(math.ceil(10.0/2)))
    if begin < 1:
        begin = 1
    end = begin + 9
    if end > page_obj.num_pages:
        end = page_obj.num_pages

    if end <= 10:
        begin = 1
    else:
        begin = end - 9

    pageList = range(begin, end+1)


    return render(request, 'index.html',
                  {'post_list':perPageList,
                   "pagelist":pageList,
                   "currentNum":num},
                  )

# 查看阅读全文功能
def detail(request, postid):
    postid = int(postid)
    # 根据postid查询帖子的详情
    post = Post.objects.get(postid)
    return render(request,'detail.heml',{"post":post})