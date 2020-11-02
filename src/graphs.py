import matplotlib as plt
import seaborn as sns

def graph(a,b,c,d):
    return sns.countplot(x=b, data=a, palette=c,order=a[b].value_counts().iloc[:d].index)

#a = the dataframe
#b = the column we want to plot
#c = colour palette
#d = number of observations we want to see. We use iloc[:] to chose the observations based on valu_counts
    #this way we can observe the main categories

def graph_hue(a,b,c,d,e):
    return sns.countplot(x=b, hue = e, data=a, palette=c,  order=a[b].value_counts().iloc[:d].index)

#apart form the previous explanation:
#e = hue, anothe variable we want to observe together with the main one