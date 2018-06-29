
#! python3

# --------- Flash Hello Future------- #

#import the flask module

from flask import Flask

#create the application object

app = Flask(__name__)

#Use decorators to link the function to a url
@app.route("/")
@app.route("/hello")

# define the view using a fuction, which returns a string

def hello_future():
	return "Hello, Future! \nStill trying to figure out how exactly Flask works in web development but soon I'll master it."

# start the development server using the run() method
if __name__ == "__main__":
	app.run()



