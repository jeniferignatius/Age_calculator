import functools
from datetime import datetime
debug = True
def debugger(function):
    @functools.wraps(function)
    def wrapper(*args,**kwargs):
        if debug:
            now= datetime.now()
            msg = now.strftime("%Y-%m-%d %H:%M:%S") + ''
            msg += function.__name__+''
            msg += str(args)[1:-2]
            msg += str(kwargs)[1:-2]
            result = function(*args)
            msg += ", result is " + result
            f = open("logfile.txt","a",encoding="utf-8")
            f.write(msg + "\n")
            f.close()
            #print(msg + "\n")
        return result
    return wrapper