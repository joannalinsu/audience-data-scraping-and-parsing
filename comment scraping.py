import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall
import urllib,re
import csv

re_h=re.compile('</?\w+[^>]*>')
csvfile = open('yelp.csv=','w',newline='')
spamwriter = csv.writer(csvfile)

for n in range (1,3):
    page = urllib.request.urlopen('https://www.bevol.cn/composition/goods/9cbf505bd66a5913c7c9adbb5d5c654f.html?p=' + str(n))
    contents = page.read() 
    soup = BeautifulSoup(contents,"html.parser")
    for tag in soup.find_all('p', class='p1'):
            string=str(tag)
            string=re_h.sub('',string)
            spamwriter.writerow([string])
csvfile.close()



