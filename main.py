from flask import Flask
from flask import request
from flask import jsonify
from bs4 import BeautifulSoup
import requests
app=Flask(__name__)
app.config['JSON_SORT_KEYS']=False
months=["January","February","March","April","May","June","July","August","September","October","November","December"]
@app.get("/")
def welcome():
    return "Welcome To Urban Dictionary API By Abhimanyu Sharma!"
@app.get("/api")
def get_word():
    query=str(request.args.get("word"))
    data=requests.post(f"https://urbandictionary.com/define.php?term={query}").content
    soup=BeautifulSoup(data,"html.parser")
    try:
        # Find Meaning
        meaning=soup.find("div",class_="meaning").text
        # Find More Meanings
        more_meanings=[]
        len_more_meanings=len(soup.find_all("div",class_="meaning"))
        for i,j in enumerate(soup.find_all("div",class_="meaning")):
            more_meanings.append(dict())
            more_meanings[i]["meaning"]=j.text
        for i,j in enumerate(soup.find_all("div",class_="example")):
            more_meanings[i]["example"]=j.text
        for month in months:
            for i,j in enumerate(soup.find_all("div",class_="contributor")):
                if month in j.text:
                    more_meanings[i]["author"]=j.text[3:j.text.find(month)].strip()
        for month in months:
            for i,j in enumerate(soup.find_all("div",class_="contributor")):
                if month in j.text:
                    more_meanings[i]["date"]=j.text[j.text.find(month):].strip()
        more_meanings=more_meanings[1:]
        # Find Example
        example=soup.find("div",class_="example").text
        # Find Author
        author_and_date=""
        for i in soup.find("div",class_="contributor"):
            for j in i.string:
                author_and_date+=j
        for i in months:
            if i in author_and_date:
                author_location=author_and_date.find(i)
                new_author=author_and_date[3:author_location].strip()
        # Find Date
        for i in months:
            if i in author_and_date:
                date_location=author_and_date.find(i)
                date=author_and_date[date_location:].strip()
        json={
            "word":query,
            "meaning":meaning,
            "example":example,
            "author":new_author,
            "date":date,
            "more_meanings":more_meanings
        }
        return jsonify(json)
    except:
        try:
            try_one_of_these_list=[]
            for i in soup.find("ul"):
                try_one_of_these_list.append(i.text)
        except:
            try_one_of_these_list=[]
        json={
            "word":query,
            "meaning":f"We Couldn't Find {query}",
            "example":None,
            "author":None,
            "date":None,
            "more_meanings":[],
            "try one of these":try_one_of_these_list
        }
        return jsonify(json)
app.run(debug=True)