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
    soup=BeautifulSoup(data)
    try:
        # Find Meaning
        meaning=soup.find("div",class_="meaning").text
        # Find Example
        example=soup.find("div",class_="example").text
        # Find Author
        author=""
        for i in soup.find("div",class_="contributor"):
            for j in i.string:
                author+=j
        author=author[3:]
        without_date_author=author.split(" ")[0]
        # Find Date
        date=author.split(" ")
        date=" ".join(date[1:])
        json={
            "word":query.title(),
            "meaning":meaning.replace("None",""),
            "example":example,
            "author":without_date_author,
            "date":date,
        }
        return jsonify(json)
    except:
        json={
            "word":query,
            "meaning":f"We Couldn't Find {query}",
            "example":"null",
            "author":"null",
            "date":"null"
        }
        return jsonify(json)
app.run(debug=True)