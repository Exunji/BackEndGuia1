from django.shortcuts import render
from django.http import HttpResponse

def dimitri(request):
    html = """<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4c/ChowChow2Szczecin.jpg/1200px-ChowChow2Szczecin.jpg" alt="dimitri">"""

    return HttpResponse(html)

def jumpscare(request):
    html ="""<img src="https://i.ytimg.com/vi/WnRrPqgKBS0/hqdefault.jpg" alt="jumpscare">"""

    return HttpResponse(html)