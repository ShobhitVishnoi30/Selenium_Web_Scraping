from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
from .form import TagClass
from .models import Tags

# Create your views here.
def showformdata(request):
    if request.method=='POST':
        f=TagClass(request.POST)
        if f.is_valid():
            result1=[]
            result=call_data(f.cleaned_data['tag'])
            result1=result
            t=f.cleaned_data['tag']
            if(len(result1)<10):
                length=len(result1)
                for i in range(length,10):
                    result1.append(0);
            sa=Tags(id=1,tag=t,tag1=result1[0],tag2=result1[1],tag3=result1[2],tag4=result1[3],tag5=result1[4],tag6=result1[5],tag7=result1[6],tag8=result1[7],tag9=result1[8],tag10=result1[9])
            sa.save()
            ta=Tags.objects.all()
            return render(request,'web_scraper1/titles.html',{'tit':ta})
    else:
        f=TagClass()
    return render(request,'web_scraper1/taginput.html',{'form':f})

def call_data(tag):
    PATH ="C:\Program Files (x86)\chromedriver.exe"
    driver =webdriver.Chrome(PATH)
    driver.get("https://medium.com/search?q="+tag) 
    titles=driver.find_elements_by_class_name("graf--title")
    tag=driver.find_elements_by_class_name("u-clearfix")
    for t in tag:
        print(t.text)
    result=[]
    for title in titles:
        result.append(title.text)
    return result

