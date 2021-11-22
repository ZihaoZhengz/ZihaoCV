"""
Name: Zihao Zheng
ID: zihaozhe 
Course number and section: 12780 A2
Homework number: 3
"""

from flask import Flask,render_template
from educationAndWork import education, work

# initiate the education experience and work experience
university=["Shanghai Ocean University","Tokyo University of Marine Science and Technology","Carnegie Mellon University"]
universityPeriod=["Sep. 2013 – Jul. 2017","Apr. 2016 – Mar. 2017","Feb. 2021 - Now"]
e=education(university,universityPeriod)
company="Baojia Environmental Construction Co., Ltd.";
workPeriod="Sep.2017 – Oct.2019"
job="Environmental Engineer"
w=work(company,job,workPeriod);
edu,time=e.showInfo();
career=w.showInfo();
app = Flask(__name__)

@app.route("/")
def main():
    return "Wanna get my CV? Please add /getCV to the url"
@app.route("/getCV")
# pass the value to index.html
def getCV():
    return render_template("index.html",edu=edu,time=time,job=career)
            
if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")
