from django.shortcuts import render
import requests
# Create your views here.
def index(request):
    try:
        if request.method=="POST":
   
            city= request.POST['city_form']
            # F=request.POST['F']
            
            url1=f"http://dataservice.accuweather.com/locations/v1/cities/search?apikey=v8MIJbgzwHaPzpTUjfNcVjVixQOf7FpG&q={city}"
        
            r=requests.get(url=url1)
            data=r.json()
            location_key=data[0]['Key']
     
            
            URL=f"http://dataservice.accuweather.com/currentconditions/v1/{location_key}?apikey=v8MIJbgzwHaPzpTUjfNcVjVixQOf7FpG"
            r=requests.get(url=URL)
            data=r.json()
     
     
            text=data[0]['WeatherText']
            final_data=data[0]['Temperature']['Metric']
            C=final_data['Unit']
            print(final_data)
            data=final_data['Value']
        
            return render(request,'index.html',{'data':data,'c':C,'city':city,'weathertext':text})
        return render(request, 'index.html')
    except:

        return render(request, 'index.html')