"""A madlib game that compliments its users."""

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
    'alpaca'
]


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


@app.route('/madlib')
def show_madlib():
    color = request.args.get("color")
    noun = request.args.get("noun")
    person = request.args.get("person")
    adjective = request.args.get("adjective")

    pets = []
    print request.args
    for arg, value in request.args.items():
        print arg
        print value
        if arg == 'pets':
            pets.append(value)
    print pets

    verb = request.args.get("verb")

    return render_template("madlib.html", color=color, noun=noun,
                           person=person, adjective=adjective, pets=pets,
                           verb=verb)

if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
