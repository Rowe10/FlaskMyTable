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

