from django.shortcuts import render

from .models import Topic

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def topic(request)