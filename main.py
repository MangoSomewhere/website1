from flask import Flask, render_template, url_for
# Flask is a class of flask which contains all the protypes that you need to build web apps with python
# It will handle all the requests

# create a variable where you will store your flask object instance
'''
The line below instatiates the class that object
'''
app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about/')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)
