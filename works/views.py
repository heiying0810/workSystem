from django.shortcuts import render

# 404页面
def page_not_found(request,exception):
    return render(request, "works/404.html")
