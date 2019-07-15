from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext']

    wordlist=fulltext.split()

    worddictionary={}

    for word in wordlist:
        if word in worddictionary:
            #increase
            worddictionary[word]+=1
        else:
            #add dictionary
            worddictionary[word]=1




    return render(request,'count.html',{'text':fulltext,'count':len(wordlist),'countwords':worddictionary})
