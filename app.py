# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Archit" # write your name
    age = "15" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def fat():
    name = "Nawal "
    age = "44"
    return render_template("father.html", name = name , age = age)


# define the route to mother webpage
@app.route("/mother")
def mot():
    age = "39" 
    name2 = "Sita"
    return render_template("mother.html", name = name2 , age = age)

# define the route to friends webpage
@app.route("/friends")
def fri():
    name3 = "friend"    
    age = "15"
    return render_template("friend.html", name = name3 , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
