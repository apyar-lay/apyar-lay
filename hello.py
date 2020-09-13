import requests
from bs4 import BeautifulSoup
from rabbit import Rabbit
import json
from pymongo import MongoClient
client = MongoClient()

client = MongoClient('mongodb://root:root@cluster0-shard-00-00.j6utm.mongodb.net:27017,cluster0-shard-00-01.j6utm.mongodb.net:27017,cluster0-shard-00-02.j6utm.mongodb.net:27017/apyar?ssl=true&replicaSet=atlas-chyjew-shard-0&authSource=admin&retryWrites=true&w=majority')
db = client.apyar
db.data.rename( "articles" )
articles = db.data

# # articles = []
# page = requests.get('https://apyarr.blogspot.com/2019/02/blog-post_29.html')
# # page = requests.get('https://apyarr.blogspot.com/2018/10/blog-post_16.html')
# soup = BeautifulSoup(page.content, "html.parser")
# # print(Rabbit.zg2uni(soup.body.find('h1','post-title entry-title').get_text().strip()))
# # print(Rabbit.zg2uni(soup.body.find('div',"post-body entry-content",itemprop="articleBody").get_text().strip()))
# # print(soup.body.find('a',id="Blog1_blog-pager-older-link")['href'])
# next_link = soup.body.find('a',id="Blog1_blog-pager-older-link")
# title = soup.body.find('h1','post-title entry-title').get_text().strip().replace('\n','').replace('\t','')
# body = soup.body.find('div',"post-body entry-content",itemprop="articleBody").get_text().strip().replace('\n','').replace('\t','')
# article = {'title':Rabbit.zg2uni(title),'body':Rabbit.zg2uni(body)}
# # articles.append(article)
# articles.insert_one(article)
# while(next_link is not None):
#     page = requests.get(next_link['href'])
#     soup = BeautifulSoup(page.content, "html.parser")
#     next_link = soup.body.find('a',id="Blog1_blog-pager-older-link")
#     title = soup.body.find('h1','post-title entry-title').get_text().strip().replace('\n','').replace('\t','')
#     body = soup.body.find('div',"post-body entry-content",itemprop="articleBody").get_text().strip().replace('\n','').replace('\t','')
#     article = {'title':Rabbit.zg2uni(title),'body':Rabbit.zg2uni(body)}
#     # articles.append(article)
#     articles.insert_one(article)

# with open("data.json", 'w', encoding='utf-8') as file:
#     json.dump(articles, file, ensure_ascii=False, indent=4) 
