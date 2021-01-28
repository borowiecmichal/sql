from connection import connect
from flask import Flask, request, render_template

from get_data import get_authors
from insert_data_to_db import dodaj_autora

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("base.html")


@app.route('/add_authors', methods=['GET', 'POST'])
def author():
    authors_lst = get_authors()
    if request.method == 'POST':
        dodaj_autora(**request.form)
    authors_lst = get_authors()
    return render_template("author.html", authors=authors_lst)


if __name__ == '__main__':
    app.run()
