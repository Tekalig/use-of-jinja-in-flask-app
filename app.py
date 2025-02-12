from flask import Flask, render_template

from moon import Moons

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/expression/')
def expressions():
    color = 'pink'
    animal_one = 'fox'
    animal_two = 'dog'
    orange_amount = 20
    apple_amount = 30
    donate_amount = 10
    first_name = 'Tekalign'
    last_name = 'Mesfin'

    kwargs = {
        'color':color,
        'animal_one':animal_one,
        'animal_two':animal_two,
        'orange_amount':orange_amount,
        'apple_amount':apple_amount,
        'donate_amount':donate_amount,
        'first_name':first_name,
        'last_name':last_name
    }
    return render_template('expressions.html', **kwargs)

@app.route('/data_structure/')
def data_structure():
    movies = [
        'life is not fair',
        'time matters',
        'hard working life'
    ]

    car = {
        'brand':'Tesla',
        'model':'Got life',
        'year':2020
    }

    moons = Moons('besu21', 'time21', 'none21', 'life21' )

    kwargs = {
        'movies':movies,
        'car':car,
        'moons':moons
    }
    return render_template('data_structures.html', **kwargs)

@app.route('/conditional/')
def conditionals():
    company = ''
    return render_template('conditionals_basics.html', company=company)
