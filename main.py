from flask import Flask, render_template, request
import random

app = Flask(
  __name__,
  template_folder='templates',  #this is for things that change
  static_folder='static',
  static_url_path='/static/'
  #things that dont change: images, javascript, stylesheets, terms and conditions, privacy policy, some other pages # So the big different here is that the static directory may be a cloud directory so it would not be here but would like cdn.mysite.com/...
)

#step 1: add your html files to templates
#step 2: attach your html files to an endpoint & function (e.g. hello_testing)
#step 3: make the data dynamic
  # a) add a variable to the function and pass it as an argument to render_template
  # b) edit the template so that it picks up the variable 
  # {{ }} displays the variable
  # {% %} displays control logic like a conditional, or a loop 
# step 4 update your template 
  # a) so that the static resources are preappended with /staticmethod
  # b) so that all the href are endpoints and not html


def pick_country():
  countries = ["France","Turkey","China","S. Korea","Japan","Morocco", "Taiwan", "Russia","USA"]  
  index = random.randint(0,len(countries)-1)
  return (countries[index], index)

@app.route("/")
def index():
  country,index = pick_country()
  return render_template("Index.html",c=country,i=index)

@app.route("/lagoon")
def lagoon():
  country,index = pick_country()
  about = "The blue lagoon is a magical hotspring in iceland"
  description= ""

  details = {"about":about,"desc":description}
  return render_template("lagoon.html",details=details)


# @ is a decorator in python -https://wiki.python.org/moin/PythonDecorators

@app.route("/en/3.2/intro/")
def hello_intro():
  return "<p>intro</P>"

@app.route("/en/3.2/intro/overview/")
def hello_intro_overview():
  return "<p>intro hello_intro_overview</P>"

@app.route("/en/3.2/")
def hello_django():
  return "<p>Django</P>"


@app.route("/countries") #THIS IS AN ENDPOINT!
def hello_countries():
  return "<p>Countries</P>"


if __name__ == "__main__": 
	app.run( 
		host='0.0.0.0', 
		port=5555
	) 