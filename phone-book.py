import pickle
import myPhoneBook as myPB
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def main():
   return render_template('main.html')

@app.route('/table')
def table():
   return render_template('table.html', table = dict)

if __name__ == '__main__':
   app.run(debug = True)