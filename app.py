from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route("/")
def home():
    dice_number = random.randint(1, 6)
    return render_template("index.html", dice=dice_number)

if __name__ == "__main__":
    app.run(debug=True)
