from io import StringIO
from contextlib import redirect_stdout
from inspect import signature, getsource
import sys, traceback

import datetime

def decorator_fun_4(fun):
    """ Function decorator that handels errors and sends them to log.txt"""
    
    def wrapper(*args,**kargs):
        try:
            f=StringIO()
            with redirect_stdout(f):
                fun(*args, **kargs)
                return fun(*args, **kargs)
            
        except Exception:
            with open("Log.txt", "a") as log:
                date = datetime.datetime.now()
                log.write("Date timestamp: {0}".format(date))
                log.write(traceback.format_exc())
                log.write('\n')
            log.close()
            
    return wrapper


#class decorator
class decorator_class_4:
    """ Class decorator that handels errors and sends them to log.txt"""
    def __init__(self,fun):
        self.fun = fun # Refers to function itself

    def __call__(self, *args, **kargs):

        try:
            f = StringIO()
            with redirect_stdout(f):
                self.fun(*args, **kargs)
        except Exception:
            with open("Log.txt", "a") as log:
                date = datetime.datetime.now()
                log.write("Date timestamp: {0}  ".format(date))
                log.write('\n')
                traceback.print_exc(file=log)
            log.close()
        


        
