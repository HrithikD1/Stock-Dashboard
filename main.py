import datetime
from datetime import date
import matplotlib.pyplot as plt
from nsepy import get_history

today = datetime.datetime.now()

#accessing the month, day, year
yy = today.year
mm=today.month
dd = today.day

print(yy)
print(mm)
print(dd)




# Stock futures (Similarly for index futures, set index = True)
stock_fut = get_history(symbol="TATASTEEl",
                        start=date(yy-1,mm+11,dd+28),
                        end=date(yy,mm,dd),
                        )

stock_fut.to_csv('file2.csv', header=True, index=True)

stock1fut = get_history(symbol="IDEA",
                        start=date(yy-1,mm+11,dd+28),
                        end=date(yy,mm,dd),
                        )

stock1fut.to_csv('file1.csv', header=True, index=True)



import pandas as pandas
from flask import Flask, render_template

app = Flask(__name__)

# route to html page - "table"
url = "http://127.0.0.1:5000/"

@app.route('/stock1')
def table():

    # converting csv to html
    data = pandas.read_csv("file2.csv")
    return render_template('table.html', tables=[data.to_html()], titles=[''])

@app.route('/stock2')
def stock2():
    data = pandas.read_csv("file1.csv")
    return render_template('table.html', tables=[data.to_html()], titles=[''])

@app.route('/')
def homepage():
    return render_template('homepage.html', url=url)

if __name__ == "__main__":
    app.run(debug=False)
