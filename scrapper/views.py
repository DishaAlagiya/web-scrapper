from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from django.http import HttpResponseRedirect
from .models import Link

def clear(request):
    Link.objects.all().delete()
    return render(request, 'scrapper/result.html')

def scrape(request): 
    
    if request.method == "POST":
        site = request.POST.get('site','') 
        if not site.startswith("http"):
            site = "https://" + site
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')
        
        for link in soup.find_all('a'):
            print(link)
            link_address = link.get('href')
            link_text = link.string
            if link_address:   # avoid None href
                Link.objects.create(address=link_address, name=link_text)

        return HttpResponseRedirect("/")
        
        
    
    data = Link.objects.all()
    context = {
        "data": data        
    }
    return render(request, 'scrapper/result.html', context)