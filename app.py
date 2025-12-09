from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/page2")
def page2():
    return render_template("page2.html")


WIN_MESSAGE = [
    "What do you want a reward?",
    "Okay....guess again.",
    "What did you really accomplish here",
    "I mean...Congratulations?",
    "You won't get it right a second time"

]

LOSE_RESPONSES = [
    "Nope. Not even close.",
    "Bro its not that hard pick the right one",
    "Try again… I believe in you. not really.",
    "Wrong! But at least you’re consistent.",
    "Your intuition must be horrible",
    "Close! …emotionally. Numerically? Not so much.",
    "The number disagrees with your choices.",
    "Plot twist: that was not it."
]


@app.route("/", methods=["GET", "POST"])
def index():
    result_message = None
    guess = None

    if request.method == "POST":
        user_input = request.form.get("guess", "").strip()

        try:
            guess = int(user_input)
        except ValueError:
            result_message = "Can you even follow instructions? 1-10 kid."
            return render_template("index.html", result=result_message, guess=None)

        if guess < 1 or guess > 10:
            result_message = "Can you even follow instructions? 1-10 kid."
        else:
            secret_number = random.randint(1, 10)

            if guess == secret_number:
                win = random.choice(WIN_MESSAGE)
                result_message = (f"<center>{win}<br>" 
                f"<center>(The number was {secret_number}.)"
                )
            else:
                funny = random.choice(LOSE_RESPONSES)
                result_message = (
                    f"<center>{funny}<br>"
                    f"<center>You guessed <strong>{guess}</strong> "
                    f"<center>The number was <strong>{secret_number}</strong>."
                )

    return render_template("index.html", result=result_message, guess=guess)


if __name__ == "__main__":
    app.run(debug=True)
