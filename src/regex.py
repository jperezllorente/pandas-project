import re

def change_re(data,what,to):
    x = data.replace(to_replace = what, value = to, regex = True)
    return x

def change(data,what,to):
    return data.replace(to_replace = what, value = to)

def equal(a,b):
    x = a.equals(b)
    return x
