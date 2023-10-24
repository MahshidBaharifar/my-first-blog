from django.shortcuts import render

# Create your views here.
def post_list(request):
    return render(request,'/home/dci-student/Desktop/excersises/django-home-project/djangogirls/blog/templates/blog/post_list.html',{})
