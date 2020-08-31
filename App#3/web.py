from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") # pass HTML to python web app it has to be in a 'templates folder'

@app.route('/about/')
def about():
    return render_template("about.html") # pass HTML to python web app it has to be in a 'templates folder'

if __name__=="__main__":
    app.run(debug=True)  

#http://xherokux.herokuapp.com/
# pip freeze
#local test before push to production 
#heroku login / info / apps
#heroku git:remote --app xherokux -> add ->commit -> push -> heroku open
