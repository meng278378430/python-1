import random
import time
import os
import requests
import easygui as eg
import re
import bs4
import scrapy
import urllib.request as ur
#eg.msgbox("开始吧")
base_url=eg.enterbox()
eg.msgbox("你要下载的网址是%s" % base_url)
def getUrls(base_url):
        res=open_url(base_url)
        #print(res)
        urls=re.findall(r"/cat/cartoons.*?page=1",res)
        return urls        
def open_url(base_url):
        headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
        html=requests.get(base_url,headers=headers)
        bs=bs4.BeautifulSoup(html.text,"html.parser")
        bs1=str(bs)
        return bs1
def get_img(html):
        print("进入get_img 函数")
        print(html)
        img_urls=re.findall(r"http.*?png",html)
        print(img_urls)
        return img_urls
def save_img(img_urls):
        for each in img_urls:
                        req=requests.get(each)
                        headers={"User-Agent":" Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"}
                        req=ur.Request(url=each,headers=headers)
                        res=ur.urlopen(req)
                        temp=res.read()
                        f_filename=each.split(".")[-2]
                        filename=f_filename.split("/")[-1]+str(time.time())+".jpg"
                        with open(filename,"wb+") as f1:
                                f1.write(temp)
                                print(filename,"保存完成")
                                               

def main():
            urls = getUrls(base_url)
            '''for each in urls:
                    #print(each+'\n')
                    print("https://www.stickpng.com"+each)
                    res=open_url("https://www.stickpng.com"+each)
                    img_urls=get_img(res)
                    save_img(img_urls)'''
if __name__=="__main__":
      main()
