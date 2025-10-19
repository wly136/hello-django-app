from django.shortcuts import render

def hello_world(request):
    """简单的Hello World视图函数"""
    return render(request, 'hello/index.html', {'message': '你好，世界！'})

def hello_name(request, name):
    """带参数的问候视图函数"""
    return render(request, 'hello/greeting.html', {'name': name})