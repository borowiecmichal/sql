from connection import connect
from flask import Flask, request,render_template

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("base.html")

@app.route('/add_authors')
def author():
    return  render_template("author.html")




if __name__ == '__main__':
    app.run()
