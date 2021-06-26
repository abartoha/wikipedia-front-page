from bs4 import BeautifulSoup
from requests import get
import pdb
import codecs
from datetime import datetime
from os import getlogin

class MainPage:
    def __init__(self):
        req = get("https://en.wikipedia.org/wiki/Main_Page")
        self.soup = BeautifulSoup(req.content,"html.parser")
        #Things that I didn't want to write inside init but needed to
        self.link_list = []
        self._tfp()
        self._tfa()
        self._itn()
        self._dyk()
        self._otd()
    def _otd(self):
        self.mp_otd = self.soup.find("div", attrs={"id":"mp-otd"})
        #self.mp_otd_img = self.mp_otd.find("div", attrs={"id":"mp-otd-img"})
        self.mp_otd_ul = self.mp_otd.find("ul")
        for i in self.mp_otd_ul.find_all("a", href=True):
            if not self.link_list.__contains__(i):
                self.link_list.append(i)
        self.mp_otd_ul_li = [i for i in self.mp_otd_ul.find_all("li")]
    def _dyk(self):
        self.mp_dyk = self.soup.find("div", attrs={"id":"mp-dyk"})
        #self.mp_dyk_img = self.mp_dyk.find("div", attrs={"id":"mp-dyk-img"})
        self.mp_dyk_ul = self.mp_dyk.find("ul")

        for i in self.mp_dyk_ul.find_all("a", href=True):
            if not self.link_list.__contains__(i):
                self.link_list.append(i)
        
        self.mp_dyk_ul_li = [i for i in self.mp_dyk_ul.find_all("li")]
    def _tfa(self):
        self.mp_tfa = self.soup.find("div", attrs={"id":"mp-tfa"})

        for i in self.mp_tfa.find_all("a", href=True):
            if not self.link_list.__contains__(i):
                self.link_list.append(i)
        #self.mp_tfa_img = self.mp_tfa.find("div", attrs={"id":"mp-tfa-img"})
        #self.mp_tfa_p = self.mp_tfa.find("p")
        #self.mp_tfa_p_a_title = self.mp_tfa_p.find("a", title=True)
        #self.mp_tfa_ul = self.mp_tfa.find("ul")
        #self.mp_tfa_ul_li = [i for i in self.mp_tfa_ul.find_all("li")]
        #self.mp_tfa_ul_li_a_href = [f"https://en.wikipedia.org{i['href']}" for i in self.mp_tfa_ul.find_all("a", href=True)]
        #return self.mp_tfa_p.text #TODO There's a last (Full article...) that I couldn't remove
    def _itn(self):
        self.mp_itn = self.soup.find("div", attrs={"id":"mp-itn"})
        #self.mp_itn_img = self.mp_itn.find("div", attrs={"id":"mp-itn-img"})
        self.mp_itn_ul = self.mp_itn.find("ul")
        for i in self.mp_itn_ul.find_all("a", href=True):
            if not self.link_list.__contains__(i):
                self.link_list.append(i)
        self.mp_itn_ul_li = [i for i in self.mp_itn_ul.find_all("li")]
        self.mp_itn_ul_li_a_href = [f"https://en.wikipedia.org{i['href']}" for i in self.mp_itn_ul.find_all("a", href=True)]
        #return self.mp_itn_ul_li
    def _tfp(self):
        self.mp_tfp = self.soup.find("div", attrs={"id":"mp-tfp"})
        self.mp_tfp_img = self.mp_tfp.find("img", src=True)['src']
        self.mp_tfp_p = self.mp_tfp.find("p")
    def tfa(self):
        print("\n============= TODAY'S FEATURED ARTICLE =======")
        #print(self.mp_tfa_p.text)
        print(self.mp_tfa.text)
    def tfp(self):
        print("\n============= TODAY'S FEATURED PICTURE =======")
        
        print(self.mp_tfp_p.text)
        print("https:"+self.mp_tfp_img)
        #print(self.mp_tfp.text)
    def itn(self):
        print("\n================ IN TODAY'S NEWS ==============")
        j = 1
        for i in self.mp_itn_ul_li:
            print(str(j)+".")
            print(i.text)
            j += 1
    def dyk(self):
        print("\r\n================= DID YOU KNOW? ===============")
        j = 1
        for i in self.mp_dyk_ul_li:
            print(f"{j}.")
            print(i.text)
            j += 1
    def otd(self):
        print("\r\n================== ON THIS DAY ================")
        j = 1
        for i in self.mp_otd_ul_li:
            print(str(j)+".")
            print(i.text)
            j += 1
    def output(self):
        time = datetime.now()
        date = time.strftime("%Y %m %d %H %M %S %A ")
        datename = time.strftime("%Y %m %d")
        with codecs.open(f"C://Users//{getlogin()}//Desktop//WIKIPEDIA-{datename}.txt","w+","utf-8") as file:
            file.write(f"Scraping time: {date}\r\n\r\n")
            file.write("\r\n======== TODAY'S FEATURED PICTURE =======\r\n\r\n")
            file.write(self.mp_tfp_p.text)
            
            file.write("\r\n\r\n")
            file.write("\r\n========== TODAY'S FEATURED ARTICLE =======\r\n\r\n")
            #file.write(self.mp_tfa_p.text)
            file.write(self.mp_tfa.text)
            file.write("\r\n\r\n")
            file.write("\r\n============= IN TODAY'S NEWS ===========\r\n\r\n")
            j = 1
            for i in self.mp_itn_ul_li:
                file.write(str(j)+".")
                file.write(i.text)
                file.write("\r\n\r\n")
                j += 1
            file.write("\r\n============== DID YOU KNOW? ============\r\n\r\n")
            j = 1
            for i in self.mp_dyk_ul_li:
                file.write(f"{j}.")
                file.write(i.text)
                file.write("\r\n\r\n")
                j += 1
            file.write("\r\n=============== ON THIS DAY =============\r\n\r\n")
            j = 1
            for i in self.mp_otd_ul_li:
                file.write(str(j)+".")
                file.write(i.text)
                file.write("\r\n\r\n")
                j += 1
            j = 1
            file.write("\r\n============= LINKS ===============\r\n")
            for i in x.link_list:
                file.write("\r\n"+str(j)+".\t"+i.text+":\r\n"+"https://en.wikipedia.org"+i['href']+"\r\n")
                j += 1
            file.write("\r\n")
            file.write("PHOTO LINK :: https:"+self.mp_tfp_img)
            file.write("\r\n")
            file.write("\r\nThanks for reading all the way through! I have a webswcraping project that scrapes all the information from the first page of wikipedia so I can post it everyday on my facebook profile. I have written the webscraping script myself and run it everyday to get worldly updates everyday. If you really want to support me consider sharing this page and promoting me. Thanks!\r\n")

            

# def page(url):
#     req = get(url)
#     soup = BeautifulSoup(req.content,"html.parser")
#     return soup

# def on_this_day(soup):
#     mp_otd = soup.find("div", attrs={"id":"mp-otd"})
#     mp_otd_img = mp_otd.find("div", attrs={"id":"mp-otd-img"})
#     mp_otd_ul = mp_otd.find("ul")
#     mp_otd_ul_li = [i for i in mp_otd_ul.find_all("li")]
#     return mp_otd_ul_li

# def did_you_know(soup):
#     mp_dyk = soup.find("div", attrs={"id":"mp-dyk"})
#     mp_dyk_img = mp_dyk.find("div", attrs={"id":"mp-dyk-img"})
#     mp_dyk_ul = mp_dyk.find("ul")
#     mp_dyk_ul_li = [i for i in mp_dyk_ul.find_all("li")]
#     return mp_dyk_ul_li

# def in_the_news(soup):
#     mp_itn = soup.find("div", attrs={"id":"mp-itn"})
#     mp_itn_img = mp_itn.find("div", attrs={"id":"mp-itn-img"})
#     mp_itn_ul = mp_itn.find("ul")
#     mp_itn_ul_li = [i for i in mp_itn_ul.find_all("li")]
#     mp_itn_ul_li_a_href = [f"https://en.wikipedia.org{i['href']}" for i in mp_itn_ul.find_all("a", href=True)]
#     return mp_itn_ul_li

# def todays_featured_article(soup):
#     mp_tfa = soup.find("div", attrs={"id":"mp-tfa"})
#     mp_tfa_img = mp_tfa.find("div", attrs={"id":"mp-tfa-img"})
#     mp_tfa_p = mp_tfa.find("p")
#     mp_tfa_ul = mp_tfa.find("ul")
#     mp_tfa_ul_li = [i for i in mp_tfa_ul.find_all("li")]
#     mp_tfa_ul_li_a_href = [f"https://en.wikipedia.org{i['href']}" for i in mp_tfa_ul.find_all("a", href=True)]
#     return mp_tfa_p.text #TODO There's a last (Full article...) that I couldn't remove

if __name__=="__main__":
    x = MainPage()
    x.output()
    
    #pdb.set_trace()