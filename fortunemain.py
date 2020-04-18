from flask import Flask, render_template
import random


app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route('show.html')
def show():
    z = ['Focus on your health and well-being.', 'Get ready for a life changing event!',
          'Sooner or later, you need to take a break', 'You will make a new friend',
          'Treat others with more compassion.']
    a = random.choice(z)
    a = a
    return render_template('show.html', a=a)



if __name__ == '__main__':
    app.run(debug=True)
