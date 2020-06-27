import json
from autocorrect import Speller
from difflib import get_close_matches
# import mysql.connector
#
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="root"
#   )
#
# print(mydb)
# mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE mydatabase")





# Translator fun
def translate(w):
  check = True
  with open('data.json') as json_file:
    data = json.load(json_file)
  w = w.lower()
  possible = ''.join(get_close_matches(w, data.keys(), 1))
  if w in data:
    return data[w]
  elif possible in data:
    while check:
      askUser = str(input("Do you mean " + possible + "? Y/N: "))
      askUser = askUser.lower()

      if askUser == 'y':
        check = False
        return data[possible]
      elif askUser == 'n':
        check = False
        return "Sorry, this word does not exist"
      else:
        print("Please, enter Y/N !")

  else:
    return "Sorry, this word does not exist"

def prettify():
  x =  str(input("Enter a word:"))
  word = translate(x)

  print(type(word) == list)
  if type(word) == list:
    for i in word:
       print(i)
  else:
    print(word)


prettify()