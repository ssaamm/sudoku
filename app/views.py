from app import app, sudoku
from forms import SudokuForm
from flask import render_template

@app.route("/", methods = ["GET", "POST"])
@app.route("/index", methods = ["GET", "POST"])
def index():
    form = SudokuForm()
    if form.validate_on_submit():
        message = ""
        if sudoku.validate(form.puzzle.data):
            message = "Valid solution!"
        else:
            message = "Invalid solution"
        return render_template("message.html", message = message)
    return render_template("sudoku_form.html", form = form)
