#Define All Validations


#Length Check

def LengthCheck(String, Max, Min):
  
  value = len(String)

  if value < Max and value > Min:
    return True
    
  else:
    return False


#Hours Format Check

def HoursCheck(String):

  value = len(String)

  if value != 8 and value != 7: #User may include a 2 digit value for hours or a single digit - must accept both for better ease of use.
    return False
  
#isolate all numbers in the string
Seconds = Mid(String, (Value - 1), Value) #xx:xx:00
Minutes = Mid(String, (Value - 3), Value - 2))#xx:00:xx
Replace(String, Mid(String, (Value - 5), Value), “”) #Removes all characters from right to left, up until hours value. This accounts for 7 and 8 length strings.
        #Isolate Numbers In The String

#Seconds = Mid(String, (value - 1), value)

