import pandas as pd
import src.graphs as gr

data = pd.read_csv(r'C:\Users\juanp\Ironhack\pandas-project\data\data_clean.csv')

#We set again 'original order' as index

data = fc.index(data,"original order")

'''Our main hipothesis is that sharks are not as dangerous as people belive, and that there is
a missconception of this animals that has led to a series of activites that are endagering them.'''


'''The first thing we will check is the countries where there have 
been more shark attacks'''

gr.graph(data, "Country", "ch:s=.25,rot=-.25", 10)
    #we want to observe the Country column of data, using the "ch:s=.25,rot=-.25" pallete and 
    #observing only the 10 main countries

'''As can be seen, and should not be a surprise, is that most attacks have taken place in locations 
of the USA, Australia and South Africa'''

    #Now we are going to check the 'Activity' column

gr.graph(data, "Activity", "icefire", 10)

'''In what refers to the focus group of sharks, it can be seen that surfers lead the way followed
by swimmers and fishers. Regarding this conclusion, ther is a theory that states that sharks see 
surfers in their boards as seals, what makes them want to take a bite, or at least check if it is
something worthy to be eaten. '''

'''Should also be noticed that, the countries in which more attack have taken place have a huge surfing 
culture, which reinforces both findings'''

'''Finally, we will check the fatality of shark attack, and to obtain a bit more of information,
we will add the 'Sex' column to the graph'''

'''In the following graph we can see that most victims are males. Maybe is not surprising as men are ususally
more careless than women, but there is way too much difference between bot sexs, so we should make any conclusions.'''


gr.graph_hue(data, "Fatal (Y/N)","rocket",2, "Sex " )
    #In this case, we have chosen to observe just the 2 main categories, becuase we are not interested in 
    #unknown events. 
    #The last variable is the hue

'''What can be seen is that most attacks are not fatal, against what most people think. This confirms the main hipothesis 
of this work, which was that shark attacks are not as fatal as people believe, and that there a is a common missunderstanding 
reagrding sharks' agrresiveness. 

The hard truth is, that this believe has led to a series of activites that are threatening to extinguish many shark species,
 and if we don't act quickly, it may be too late'''
