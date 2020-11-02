import re

def null(a):
    x = a.isnull().values.any()
    return x