import os
from datetime import datetime


from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev', # this keeps data safe - it is used to allow flask to communicate with external applications [THIS SHOULD BE CHANGED IF YOU WANT TO PUT THIS PROJECT PUBLIC] - - dev is fine for
        



    )
    
    #Add Database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    #models

    from . models import  Personal
    from . models import  Clients
    from . models import  timeWorked
    from . models import  timeTable

    #Import Validations

    from . models import LengthCheck

    #import html variables

    name = ""
    bName = ""
    accNum = ""
    sortCode = ""
    hrly = ""
    mGoal = ""



    #Create

    with app.app_context():
        db.create_all()




    if test_config is None:
         #will load the instance config, if it exists, when you are not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    #app.route is a decorator that turns a regular python function into a flask view function

    # a simple page that says hello
    @app.route('/mainpage')#URL extention
    def mainpage():# function connected to the URL
        return render_template('mainPage.html') #goes to templates folder and loads file

    @app.route('/settings', methods=['POST', 'GET'])#URL extention
    
    def settings():# function connected to the URL that handles personal settings
        if request.method == 'POST':
            nameInput = request.form['Name']

            if LengthCheck(nameInput, 30, 3) == True:
                 newName = Personal(name=nameInput)
            else:
                return "Error Nope"


            newName = Personal(name=nameInput)

            #try and commit potential new data to database
            try:
                db.session.add(newName)
                db.session.commit()
                return redirect('/settings')
            except:
                return "There was an error commiting to database"
        else: #fired if you just open the page

            return render_template('settings.html', Name=name, bName=bName, accNum=accNum, sort=sortCode, hrly=hrly, mGoal=mGoal) #goes to templates folder and loads file

    @app.route('/invoice')#URL extention
    def invoice():# function connected to the URL
        return render_template('invoice.html') #goes to templates folder and loads file
    
    @app.route('/login')#URL extention
    def login():# function connected to the URL
        return render_template('login.html') #goes to templates folder and loads file

    return app


