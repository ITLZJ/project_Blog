#coding=utf-8
from django.db.models import Count

from blog.models import Post

def getrightInfo(request):
    # 类名进行分组,获取分类信息
    r_catepost=Post.objects.values('category__cname','category').annotate(c=Count('*')).order_by('-c')

    # 获取近期文章
    r_recent = Post.objects.all().order_by('-created')[:3]

    # 获取日期归档信息
    from django.db import connection
    cursor = connection.cursor()
    cursor.execute("SELECT created,COUNT('*') FROM t_post GROUP BY DATE_FORMAT(created,'%Y-%m');")
    r_file = cursor.fetchall()
    return {'r_catepost':r_catepost,'r_recent':r_recent,'r_file':r_file}