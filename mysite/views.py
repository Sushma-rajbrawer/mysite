from django.http import HttpResponse
from django.shortcuts import render
from . import urls

def index(request):
  return render(request,'index.html')

def about(request):
    return HttpResponse("about hello world")

def home(request):
    return HttpResponse('''home <a href="http://127.0.0.1:8000/capitalize"> back to captalize</a>''')

def capitalize(request):
    return HttpResponse("capitalize")
    
def ex1(request):
    s='''<h2> Navigation Bar <br> </h2>
    <a href= "https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9" > Django Code With Harry Bhai </a><br>
    <a href="https://www.facebook.com/"> Facebook </a> <br>
    <a href="https://www.flipkart.com/"> Flipkart </a> <br>
    <a href="https://www.hindustantimes.com/"> News </a> <br>
    <a href="https://www.google.com/"> Google </a> <br>'''
    return HttpResponse(s)

    
def capfirst(request):
    return HttpResponse("capfirst")

    
def charcount(request):
    return HttpResponse("charcount")

def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover','off')
    spaceremover=request.POST.get('spaceremover','off')
    
    if(removepunc == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed

    if(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
        

        

    if(newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'removed newline', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
    

    if(spaceremover=="on"):
        analyzed = ""
        for index,char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char 

        params = {'purpose': 'spaces removed', 'analyzed_text': analyzed}
        # Analyze the text
        djtext=analyzed
    if(removepunc!= "on" and fullcaps!="on" and newlineremover!="on" and spaceremover!="on"):
        return HttpResponse("error")


    return render(request, 'analyze.html', params)
   
      

    


       
           
           
  




    


   

    

    
