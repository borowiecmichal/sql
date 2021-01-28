from connection import connect
from flask import Flask, request, render_template
from insert_data_to_db import dodaj_autora

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("base.html")


@app.route('/add_authors', methods=['GET', 'POST'])
def author():
    if request.method == 'POST':
        dodaj_autora(**request.form)
    return render_template("author.html")


if __name__ == '__main__':
    app.run()
