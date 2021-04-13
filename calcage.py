from debugger import debugger
from datetime import date,datetime
from dateutil import relativedelta as datediff

query = "Please give your age in this format 1.1.1990:"

@debugger
def agecalculate(born):
    d1= datetime.strptime(born,"%d.%m.%Y").date()
    d2= date.today()
    d= datediff.relativedelta(d2,d1)
    result = "{0.years} y {0.months} mm".format(d)
    print("Age:",result)
    return result

def agequery():
    finished = False
    age = ""
    while not finished:
        try:
            born = input(query)
            datetime.strptime(born,"%d.%m.%Y")
            age = agecalculate(born)
            finished = True
        except ValueError:
            print("Error")
        finally:
            print("Question is asked, Age is "+age+".\n")
    return age

