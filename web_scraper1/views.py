from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from django.shortcuts import render
from .form import TagClass
from .models import Tags
import os


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
    chrome_options=webdriver.ChromeOptions()
    chrome_options.binary_location=os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver=webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"),chrome_options=chrome_options)
    driver.get("https://medium.com/search?q="+tag)
    driver.get("https://medium.com/search?q="+tag) 
    titles=driver.find_elements_by_class_name("graf--title")
    details=driver.find_elements_by_class_name("graf--trailing")
    names=driver.find_element_by_class_name("js-postListHandle")
    res=names.text
    result1=[]
    authors=[]
    dates=[]
    res1=res.split("responses")
    spt_char="\n"
    even=int(0)
    for i in res1:
        temp=i.split(spt_char)
        re=spt_char.join(temp[:3]), spt_char.join(temp[3:])
        re1=list(re)
        for j in re1:
            temp1=j.split("\n")
            temp2=list(temp1)
            if even%2==0:
                q=int(0)
                for k in temp2:
                    if k!='':
                        if q==0:
                            authors.append(str(k))
                            q=1
                        elif q==1:
                            dates.append(str(k))
                            q=2
            even=even+1 
    print(str(authors))
    print(str(dates))                        
    for t in details:
        result1.append(t.text)
    if(len(authors)<10):
        length=len(authors)
        for i in range(length,10):
            authors.append(0)
    if(len(dates)<10):
        length=len(dates)
        for i in range(length,10):
            dates.append(0)
    if(len(result1)<10):
        length=len(result1)
        for i in range(length,10):
            result1.append(0);
    sa=Tags(id=4,tag="Description",tag1=result1[0],tag2=result1[1],tag3=result1[2],tag4=result1[3],tag5=result1[4],tag6=result1[5],tag7=result1[6],tag8=result1[7],tag9=result1[8],tag10=result1[9])
    sa.save()
    sa1=Tags(id=2,tag="Authors",tag1=authors[0],tag2=authors[1],tag3=authors[2],tag4=authors[3],tag5=authors[4],tag6=authors[5],tag7=authors[6],tag8=authors[7],tag9=authors[8],tag10=authors[9])
    sa1.save()
    sa2=Tags(id=3,tag="Dates",tag1=dates[0],tag2=dates[1],tag3=dates[2],tag4=dates[3],tag5=dates[4],tag6=dates[5],tag7=dates[6],tag8=dates[7],tag9=dates[8],tag10=dates[9])
    sa2.save()
    result=[]
    for title in titles:
        result.append(title.text)
    return result



