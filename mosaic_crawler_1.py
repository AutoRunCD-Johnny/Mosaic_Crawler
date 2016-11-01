import urllib
import urllib2
import cookielib
import requests
from bs4 import BeautifulSoup

cookie=cookielib.MozillaCookieJar('cookie.txt')
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
#create new "open method"
url = "https://epprd.mcmaster.ca/psp/prepprd/EMPLOYEE/EMPL/?&cmd=login&languageCd=ENG"
#user_agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
#headers = { 'User-Agent' : user_agent }  
values = {"userid":"your_macid","pwd":"your_password"}  
data = urllib.urlencode(values)
#encode the postdata
result=opener.open(url,data)
cookie.save(ignore_discard=True, ignore_expires=True)

term=2151#year 2015 spring term (1)
stuid=001401391#student id
grade_url="https://csprd.mcmaster.ca/psc/prcsprd/EMPLOYEE/HRMS_LS/c/SA_LEARNER_SERVICES.SSR_SSENRL_GRADE.GBL?ACAD_CAREER=UGRD&EMPLID="+str(stuid)+"&INSTITUTION=MCMST&STRM="+str(term)+"&PAGE=SSR_SSENRL_TERM"
result=requests.get(grade_url,cookies=cookie)
#f=open("test1.txt",'w')
#f.write(result.text)

soup=BeautifulSoup(result.text,'lxml')
grade_raw=soup.find_all('span',class_="PSEDITBOX_DISPONLY")
grade_lst=[]
j,k=0,0
for i in grade_raw:
    if j%4==0:
        grade_lst.append({})
        grade_lst[k]['course']=i.get_text()
    elif j%4==1:
        grade_lst[k]['unit']=i.get_text()
    elif j%4==2:
        grade_lst[k]['grading status']=i.get_text()
    elif j%4==3:
        grade_lst[k]['grade point']=i.get_text()
        k+=1
    j+=1
print grade_lst
