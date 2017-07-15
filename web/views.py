# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
import _json
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, reverse
from django.conf import settings

def Index(request):
    '''
    首页
    :param request:
    :return:
    '''
    return render(request, 'web/index.html')


def Articles(request, pk):
    '''
    文章列表页
    :param request:
    :param pk:
    :return:
    '''
    return render(request, 'web/articles.html')

def Article(request):
    '''
    文章页
    :param request:
    :return:
    '''
    return render(request, 'web/article.html')

def About(request):
    '''
    关于页
    :param request:
    :return:
    '''
    return render(request, 'web/about.html')


def get_articles(request):
    success = {
        'rtnCode': 0,
        'rtnMsg': 'ok',
        'data': {
            'articles': [
                {
                    'id': 'id',
                    'title': '标题1',
                    'author': '周智',
                    'digest': '文章摘要文章摘要文章摘要',
                    'pub_time': 1499497266249, # 发布时间 long
                    'content': '段落1\n段落2',
                    'view': 0 # 阅读数
                },
                {
                    'id': 'id',
                    'title': '标题2',
                    'author': '周智',
                    'digest': '文章摘要文章摘要文章摘要',
                    'pub_time': 1499497266249,  # 发布时间 long
                    'content': '段落1\n段落2段落1\n段落2段落1\n段落2',
                    'view': 1000  # 阅读数
                }
            ]
        }
    }
    return JsonResponse(success)


def get_article(request):
    success = {
        'rtnCode': 0,
        'rtnMsg': 'ok',
        'data': {
            'id': 'id',
            'title': '标题1',
            'author': '周智',
            'digest': '文章摘要文章摘要文章摘要',
            'pub_time': 1499497266249,            # 发布时间 long
            'content': '段落1\n段落2',
            'view': 0
        }
    }
    return JsonResponse(success)


def add_article(request):
    pass

# @csrf_exempt
# def GetComment(request):
#     """
#     接收网易云跟帖评论消息， post方式回推
#     :param request:
#     :return:
#     """
#     arg = request.POST
#     data = arg.get('data')
#     data = _json.loads(data)[0]
#     title = data.get('title')
#     url = data.get('url')
#     source_id = data.get('sourceId')
#
#     if source_id:
#         url = reverse("web:detail", kwargs={'pk': 1})
#         article = Article.objects.get(pk=source_id)
#         article.commenced()
#
#     comments = data.get('comments')[0]
#     content = comments.get('content')
#     user = comments.get('user').get('nickname')
#
#     Comment(
#         title=title,
#         source_id=source_id,
#         user_name=user,
#         url=url,
#         comment=content
#     ).save()
#
#     return JsonResponse({"status": "ok"})
#
#
# def detail(request, pk):
#     """
#     博文详情
#     :param request:
#     :param pk:
#     :return:
#     """
#     article = get_object_or_404(Article, pk=pk)
#     article.viewed()
#     return render(request, 'web/detail.html', {"html_title": article.title,
#                                                 "article": article,
#                                                 "source_url": settings.HOST + request.path})
#
# def search(request):
#     """
#     搜索
#     :param request:
#     :return:
#     """
#     key = request.GET['key']
#     article_list = Article.objects.filter(title__contains=key)
#     return render(request, 'web/search.html',
#                   {"html_title": u"搜索'{}'".format(key), "article_list": article_list, "key": key})
#
#
#
# def tag(request, name):
#     """
#     标签
#     :param request:
#     :param name
#     :return:
#     """
#     article_list = Article.objects.filter(tag__tag_name=name)
#     return render(request, 'web/tag.html', {"html_title": u"{}标签".format(name),
#                                              "article_list": article_list,
#                                              "tag": name})