# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    #get the text
    t1=request.POST.get('text', 'default')
    #checking checkbox value
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps', 'off')
    newlineremover=request.POST.get('newlineremover', 'off')
    extraspaceremover=request.POST.get('extraspaceremover', 'off')
    charcount=request.POST.get('charcount', 'off')
    #analyzing the text
    if(removepunc=="on"):
        analyzed=""
        punctuations='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in t1:
            if char not in punctuations:
                analyzed+=char
        para={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        
        t1=analyzed
        # return render(request, 'analyzed.html', para)
    
    if(fullcaps=="on"):
        analyzed=""
        for char in t1:
            analyzed+=char.upper()
        para={'purpose':'UPPERCASE','analyzed_text':analyzed}

        t1=analyzed
        # return render(request, 'analyzed.html', para)

    if(newlineremover=="on"):
        analyzed=""
        for char in t1:
            if char!="\n" and char!="\r":
                analyzed+=char
        para={'purpose':'New Lines Removed','analyzed_text':analyzed}

        t1=analyzed
        # return render(request, 'analyzed.html', para)

    if(extraspaceremover=="on"):
        analyzed=""
        for index, char in enumerate(t1):
            if not(t1[index] == " " and t1[index+1] == " "):
                analyzed+=char
        para={'purpose':'Space Removed','analyzed_text':analyzed}

        t1=analyzed
        # return render(request, 'analyzed.html', para)

    if(charcount=="on"):
        i=0
        for index, char in enumerate(t1):
            if t1[index] == char:
                i+=1
        para={'purpose':'Character count','analyzed_text':analyzed, 'count':i}

        t1=analyzed
        # return render(request, 'analyzed.html', para)
    if(removepunc!="on" and charcount!="on" and fullcaps!="on" and extraspaceremover!="on" and newlineremover!="on"):
        return HttpResponse("Bye")

    return render(request, 'analyzed.html', para)
        