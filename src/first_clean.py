def null(data):
    data.isnull().values.any()

def dropnan(a):
    a.dropna(0, how = 'all')
    

def index(data,b):
    data.set_index(b)

def order(data):
    return data.sort_values(ascending = True)
     
    