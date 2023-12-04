# Author- Mayank Singh Gawer

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    rtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspcaeremover = request.POST.get('extraspcaeremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if removepunc == "on":
        punctuations = '''!@#$%^&*()_-+={}[]:;""''<>,.?/|'''
        analyzed = ""
        for char in rtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        rtext = analyzed
        # return render(request, 'analyze.html', params)
    if fullcaps == "on":
        analyzed = ""
        for char in rtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'UPPERCASE', 'analyzed_text': analyzed}
        rtext = analyzed
        # return render(request, 'analyze.html', params)
    if newlineremover == "on":
        analyzed = ""
        for char in rtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Remove new line', 'analyzed_text': analyzed}
        rtext = analyzed
        # return render(request, 'analyze.html', params)
    if extraspcaeremover == "on":
        analyzed = ""
        for index, char in enumerate(rtext):
            if not (rtext[index] == " " and rtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'Remove extra spaces', 'analyzed_text': analyzed}
        rtext = analyzed
        # return render(request, 'analyze.html', params)
    if charcount == "on":
        analyzed = len(rtext)
        params = {'purpose': 'Character count', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspcaeremover != "on" and charcount != "on":
        return HttpResponse("Error: please select at least one operation and try again")

    return render(request, 'analyze.html', params)
