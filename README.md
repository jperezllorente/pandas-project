# PANDAS PROJECT -SHARK ATTACK

## Objective

The main objective of this project was to clean a dataframe we imported dorm Kaggle (https://www.kaggle.com/teajay/global-shark-attacks), 
after what we had to carry out an analysis based on a hipothesis we set at the beggining. 

My hipothesis was that sharks were not as dangerous as people thought. 

## Sources

https://regexr.com/3cr6f - to check my regular expresions for finding and replacing patterns in the dataframe
The pandas, matplotlib and seaborn manuals from which I have extracted information of how to treat with NaN, droping columns, reordering the dataframe and plotting the information 
in a proper way. 
Also, I have used this line of code of mwaskom from Stackoverflow:
```import seaborn as sns
    titanic = sns.load_dataset("titanic")
    sns.countplot(y="deck", hue="class", data=titanic, palette="Greens_d",
                  order=titanic.deck.value_counts().iloc[:3].index)```


## Conclusions

The results have allowed me to accept my initial hipothesis, as most of the attacks have not been fatal. 

## Things to do better

Write a more efficient code (instead of writting tens of lines)
Being able to identify patterns quicker and easier than manually
Improve visualization
Learn more cleaning techniques
