from flask.ext.wtf import Form
from wtforms import TextAreaField, SubmitField

class SudokuForm(Form):
    puzzle = TextAreaField("Puzzle")
    submit = SubmitField("Check")
