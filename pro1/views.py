#myfirstprojects
from django.http import HttpResponse
from django.shortcuts import render

#def home(request):
#   params={'name':'nikhil','place':'mars'}
#   return render(request,'index.html',params)
def home(request):
    return render(request,'index.html')

def analyze(request):
    #toget the values from html form
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    purpo=""
    if removepunc == "on":
        punctuations= '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        purpo=purpo + "Removed punctuations + "


    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        djtext = analyzed
        purpo=purpo + "Changed To Uppercase + "


    if newlineremover == "on":
        analyzed=""
        for char in djtext:
            if char != "\n" and char !="\r":
                analyzed = analyzed + char
        djtext = analyzed
        purpo= purpo + "Removed NewLines + "


        # Analyze the text
    if (extraspaceremover == "on"):
        analyzed=""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        djtext=analyzed
        purpo=purpo + "extra spaces removed + "
    params ={'purpose': purpo, 'analyzed_text': analyzed}
        # Analyze the text
    if(removepunc != "on" and fullcaps !="on" and newlineremover !="on" and extraspaceremover !="on"):
        return HttpResponse("error")
    else:
        return render(request, 'analyze.html', params)


#def capitalizefirst(request):
 #   return HttpResponse("capitalizefirst")

#def newlineremove(request):
 #   return HttpResponse("newlineremove")

#def spaceremove(request):
 #   return HttpResponse("spaceremove")

#def charcount(request):
#   return HttpResponse("charcount")

