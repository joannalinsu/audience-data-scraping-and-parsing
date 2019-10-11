import urllib
import re
from bs4 import BeautifulSoup
from distutils.filelist import findall



for n in range (1,3):
    m=(n-1)*20
    page = urllib.request.urlopen('https://www.yelp.com/biz/daikokuya-little-tokyo-los-angeles?start='+str(m))
    contents = page.read()
    soup = BeautifulSoup(contents,"html.parser")
    for i in soup.find_all ("div",{"class":"biz-rating biz-rating-large clearfix"}):
        i = rating_count
        rating_count=rating_counter[0].div.div["title"]
        rating_count=(int(rating_count[0]))
        print(i)
