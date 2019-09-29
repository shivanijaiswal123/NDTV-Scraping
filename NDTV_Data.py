import requests
from bs4 import BeautifulSoup
from pprint import pprint

def getUrl():
    url="https://www.ndtv.com/india?pfrom=home-mainnavgation"
    response=requests.get(url)
    soup=BeautifulSoup(response.text,"html.parser")

    main_div=soup.find("div",class_="ins_left_rhs")
    find_lis=main_div.findAll("li")
    dictionary={}
    new=[]
    for index in find_lis:
        try:
            url=index.find("div",class_="new_storylising_img").a["href"]
            new.append(url)
        except AttributeError:
            continue
    return new
url_list=getUrl()

def Url_detail(urls):
    new_list=[]
    main_dict={}
    for index in urls:
        new=[]
        dictionary={}
        res=requests.get(index)
        soup=BeautifulSoup(res.text,"html.parser")

        headline=soup.find("div",class_="ins_lftcont640 clr")
        try:
            title=headline.find("div",class_="ins_headline").h1.get_text()

            date_list=soup.find("div",class_="ins_dateline").get_text()
            j=date_list.split("|")
            date=(j[2])

            outher=(j[1])

            pragraph=soup.find("div",class_="ins_lftcont640 clr")
            pra=pragraph.findAll("p")
            for i in pra:
                pragraphs = i.get_text()
                new.append(pragraphs)
                            
            dictionary["pragraph"]=new
            dictionary["heading"]=title
            dictionary["aouther"]=outher
            dictionary["date"]=date
            print (" ")
            pprint (dictionary)
            new_list.append(dictionary)
        
        except AttributeError:
            continue
        except TypeError:
            continue
    main_dict["NDTV_DATA"]=new_list
    return main_dict
pprint(Url_detail(url_list))