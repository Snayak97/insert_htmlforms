from django.shortcuts import render

# Create your views here.
from app.models import *
from django.http import HttpResponse

def insert_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['name']
        url=request.POST.get('url')

        To=Topic.objects.get(topic_name=tn)
        Wo=Webpage.objects.get_or_create(topic_name=To,name=name,url=url)[0]
        Wo.save()
        return HttpResponse('webpages is inserted')

    return render(request,'insert_webpage.html',d)


def insert_Acess(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    if request.method=='POST':
        name=request.POST['name']
        date=request.POST['date']
        author=request.POST['author']
        Wo=Webpage.objects.get(name=name)
        Ao=AcessRecord.objects.get_or_create(name=Wo,date=date,author=author)[0]
        Ao.save()
        return HttpResponse(' Acess is inserted')

    return render(request,'insert_Acess.html',d)





#retive the webpage
def retrive_webpage(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    if request.method=='POST':
        MLTS=request.POST.getlist('topic')
        WOS=Webpage.objects.none()
        for i in MLTS:
            WOS=WOS| Webpage.objects.filter(topic_name=i)
        d1={"WOS":WOS}
        return render(request,'display_webpage.html',d1)
    return render(request,'retrive_webpage.html',d)

def retrive_Acess(request):
    WTO=Webpage.objects.all()
    d={'WTO':WTO}
    if request.method=='POST':
        MLWS=request.POST.getlist('name')
        print(MLWS)
        AOS=AcessRecord.objects.none()
        for i in MLWS:
            AOS=AOS | AcessRecord.objects.filter(id=i)
        d1={"AOS":AOS}
        return render(request,'display_Acess.html',d1)

    return render(request,'retrive_Acess.html',d)





#checkbox
def chekbox(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}
    return render(request,'chekbox.html',d)

def checkbox_Acess(request):
    LWO=Webpage.objects.all()
    d={'LWO':LWO}
    return render(request,'checkbox_Acess.html',d)