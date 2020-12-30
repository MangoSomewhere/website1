from flask import Flask, render_template, url_for
# Flask is a class of flask which contains all the protypes that you need to build web apps with python
# It will handle all the requests
'''
PROBLEMS: deploying the web application to Heroku
2020-12-28T19:17:12.640311+00:00 heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/" host=dreweb.herokuapp.com request_id=02163f07-7c57-42e3-9b97-eee835b6b473 fwd="23.105.160.147" dyno= connect= service= status=503 bytes= protocol=https
2020-12-28T19:17:13.099311+00:00 heroku[router]: at=error code=H14 desc="No web processes running" method=GET path="/favicon.ico" host=dreweb.herokuapp.com request_id=1f784acd-645d-480d-a554-d2fafde03ab9 fwd="23.105.160.147" dyno= connect= service= status=503 bytes= protocol=https


'''
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
