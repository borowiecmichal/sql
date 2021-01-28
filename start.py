from connection import connect
from flask import Flask, request, render_template

from get_data import get_authors, get_books
from insert_data_to_db import dodaj_autora, add_book

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("base.html")


@app.route('/add_authors', methods=['GET', 'POST'])
def author():
    if request.method == 'POST':
        dodaj_autora(**request.form)
    authors_lst = get_authors()
    return render_template("author.html", authors=authors_lst)

@app.route('/add_books', methods=['POST', 'GET'])
def book():
    if request.method == 'POST':
        add_book(**request.form)
    books_lst = get_books()
    return render_template('book.html', books=books_lst)


if __name__ == '__main__':
    app.run()
