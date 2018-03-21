"""A madlib game that compliments its users."""

from random import choice
from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]

ADJECTIVES = ['vivacious', 'explosive', 'slumbery', 'awesome', 'cool']

PETS = [
    'dog', 'cat', 'balloonicorn', 'magical ferret', 'worm', 'snake', 'yak',
    'alpaca', 'turtle'
]
MADLIBS = ["madlib1.html", "madlib2.html"]


@app.route('/')
def start_here():
    """Display homepage."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    return render_template("greet.html",
                           person=player)


@app.route('/game')
def show_madlib_form():
    player_choice = request.args.get("yes-no")
    if player_choice == 'no':
        return render_template("goodbye.html")
    else:
        return render_template("game.html", adjectives=ADJECTIVES, pets=PETS)


@app.route('/madlib', methods=["GET", "POST"])
def show_madlib():
    if request.method == 'GET':
        user_input = request.args
    else:
        user_input = request.form

    color = user_input.get("color")
    noun = user_input.get("noun")
    person = user_input.get("person")
    person2 = user_input.get("person2")
    person3 = user_input.get("person3")
    adjective = user_input.get("adjective")
    verb = user_input.get("verb")

    pets = user_input.getlist("pets")

    return render_template(choice(MADLIBS), color=color, noun=noun,
                           person=person, person2=person2, person3=person3,
                           adjective=adjective, pets=pets, verb=verb)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
