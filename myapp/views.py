
from random_address import real_random_address
import requests
from django.http import HttpResponse
from myapp.models import Search
from django.shortcuts import redirect, render
from .models import Search


# Create your views here.
def index(request):
    return render(request,"index.html")
def search(request):
    return render(request,"search.html")
    

def test(request):
    #save the word entered
    a=request.POST['name']
    
    print(a)
    #find the long and latitude of the place
    url="http://api.positionstack.com/v1/forward?access_key="
    key="0615aeae88aa85c64a664d2bc9783fe2&query="
    
    url=url +key +a
    #url="http://api.positionstack.com/v1/forward?access_key
    
    response=requests.get(url).json()
    print(response['data'][0]['longitude'])
    
    longi=response["data"][0]['longitude']
    lat=response['data'][0]['latitude']
   
    url1="https://www.google.com/maps/@?api=1&map_action=pano&pano=tu510ie_z4ptBZYo2BGEJg&viewpoint=48.857832%2C2.295226&heading=-45&pitch=38&fov=80"
    url="https://www.google.com/maps/@?api=1&map_action=pano&viewpoint="
    
    url=url+str(lat)+"%2C"+str(longi)
    return redirect(url)
def random(request):
    a=real_random_address()
    print(a)
    city=a["city"]
    print(city)
    url="http://api.positionstack.com/v1/forward?access_key="
    key="0615aeae88aa85c64a664d2bc9783fe2&query="
    
    url=url +key +city
    #url="http://api.positionstack.com/v1/forward?access_key
    
    response=requests.get(url).json()
    
    long=response["data"][0]['longitude']
    lat=response['data'][0]['latitude']
   
    url1="https://www.google.com/maps/@?api=1&map_action=pano&pano=tu510ie_z4ptBZYo2BGEJg&viewpoint=48.857832%2C2.295226&heading=-45&pitch=38&fov=80"
    url="https://www.google.com/maps/@?api=1&map_action=pano&viewpoint="
    
    url=url+str(lat)+"%2C"+str(long)
    return redirect(url)


