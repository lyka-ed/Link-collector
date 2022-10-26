from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect


# Create your views here.

def scrape(request):
   if request.method == "POST":
      site = request.POST.get('site','')
      
      web = requests.get(site)
      soup = BeautifulSoup(web.text,'html.parser')
   
   
      for link in soup.find_all('a'):
         link_address = link.get('href')
         link_text = link.string
         Link.objects.create(address=link_address,name=link_text)
      return HttpResponseRedirect('/')  
   else: 
      data = Link.objects.all() 
    
   return render(request, 'webscrapper/result.html', {'data':data})
       
       
def clear(request):
   Link.objects.all().delete()
   return render(request,'webscrapper/result.html')      
       