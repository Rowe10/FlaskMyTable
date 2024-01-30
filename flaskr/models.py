from . import db

#Firstly Define All Validations


def LengthCheck(String, Max, Min):
  
  value = len(String)

  if value < Max and value > Min:
    return True
    
  else:
    return False

        #Hours Format Check

def HoursCheck(String):

  value = len(String)

  if value != 8 and value != 7:
    return False

        #Isolate Numbers In The String

#Seconds = Mid(String, (value - 1), value)


 #Create db model

# Validation checks will be carried out in python
class Personal(db.Model):
    
    __tablename__ = 'Personal'

    personalID = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200))
    bankName = db.Column(db.String(200))
    accountNumber = db.Column(db.String(200))
    sortCode = db.Column(db.String(200))
    hourlyRate = db.Column(db.String(200))
    monthlyGoal = db.Column(db.String(200))

    

# Create a function to return a string when we add something

    

class Clients(db.Model):


    __tablename__ = 'Clients'

    clientID = db.Column(db.Integer, primary_key = True)
    clientName = db.Column(db.String(200))
    hoursAgreed = db.Column(db.String(200))
    hoursCompleted = db.Column(db.String(200))
    editEnabled = db.Column(db.Boolean)



class timeWorked(db.Model):

    
    __tablename__ = 'timeWorked'


    logID = db.Column(db.Integer, primary_key = True)
    ClientID = db.Column(db.String(200), db.ForeignKey(Clients.clientID))
    Title = db.Column(db.String(200))
    hoursCompleted = db.Column(db.String(200))
    editEnabled = db.Column(db.Boolean)
    timeCompleted = db.Column(db.String(200))



class timeTable(db.Model):

    
    __tablename__ = 'timeTable'


    TableID = db.Column(db.Integer, primary_key = True)
    clientID = db.Column(db.String(200), db.ForeignKey(Clients.clientID))
    Title = db.Column(db.String(200))
    timeStarted = db.Column(db.String(200))
    timeEnded = db.Column(db.String(200))
    editEnabled = db.Column(db.Boolean)
    currentState = db.Column(db.String(200))
    actualTimeCompleted = db.Column(db.String(200))
    imported = db.Column(db.String(200))
    Colour = db.Column(db.String(200))



