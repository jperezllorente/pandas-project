import src.first_clean as fc
import src.regex as rg
import src.abb as ab


import pandas as pd

data = pd.read_csv("C:\\Users\\juanp\\Ironhack\\pandas-project\\data\\attacks.csv", encoding='cp1252')


fc.null(data) #This will tell us if there are any NaN in the dataset.

data_clean = data.dropna(0, how = 'all') #With this function we eliminate all observations
                 #that have more that three NaN
                 #This dataframe will be called data_clean


#There are certain columns that will not offer any information we could use for the analysis, so we proceed with deleting them
data_clean = data_clean.drop(["Unnamed: 22", "Unnamed: 23", "Location", "Name", "Species ", "Investigator or Source", "pdf", "href", "href formula","Age", "Date"], axis = 1)

#Another important issue is, that some columns still  have NaN, but we cannot use the same method for all.
#Next, we will fill NaN with 'Unknown', as they belong to columns form which we cannot guees their value

data_clean[["Case Number", "Type", "Country", "Area", "Activity", "Injury"
                         , "Case Number.1", "Case Number.2","Sex ", "Fatal (Y/N)"]] = data_clean[["Case Number", "Type", "Country", "Area", "Activity", "Injury"
                         , "Case Number.1", "Case Number.2","Sex ", "Fatal (Y/N)"]].fillna("Unknown") 

#In the case of 'Year' and 'Time' we're going to fill NaN values with the previous one, as we assume that they
#follow a certain order, and doing this is better that filling them with 'NONE'

data_clean[["Time", "Year"]] = data_clean[["Time", "Year"]].fillna(method ='ffill')

#Once we have solved the problem of the NaN, we're going to change the index of the dataframe
#In order to do so, we use .set_index().
#We chose "original order" column as index, because is the best option if we want to acces certain cases directly

data_clean = fc.index(data_clean,"original order")

#The next step will be to check the different columns looking for things thst need to be changed

#1. 'Year' 

fc.order(data_clean.Year)  #the 'Year' column seems to be fine as it is

#2. 'Country'

    #The first thing will be to change lowercase names to uppercase
    data_clean.Country = rg.change_re(data_clean.Country, r'[a-z]',r'[A-Z]')

    #Delete white spaces at the beggining
    data_clean.Country = rg.change_re(data_clean.Country, r'\s*', '')

    #Change CEYLON (SRI LANKA) to SRI LANKA - here we delete the braquets
    data_clean.Time = rg.change_re(data_clean.Country, r'\s\(\w{3}\s\w{5}\)', '')

    #And now we change CEYLON to SRI LANKA
    data_clean.Time = rg.change(data_clean.Country, 'CEYLON', 'SRI LANKA')

    #Delete de '?' at the end of certain countries

    data_clean.Time = rg.change_re(data_clean.Country, r'\?$', '')

    #Change ST MAARTIN to ST MARTIN
    data_clean.Time = rg.change(data_clean.Country, 'MAARTIN', 'MARTIN')

    #This is badly done because a mistake I made i the first step. I have to check it so I wont write it down

    
#3. 'Time'

    #working between time ranges is not going to be helpful, so we are going to use the lower hour for this analysis
    #first, we delete the section that goes after '--'

    data_clean.Time = rg.change_re(data_clean.Time, r'(s\--\s\w{2}\w\w{2})','')

    #Next, we are going to change all the words such as Afternoon, Morning and Night into 00h00 format
    #The hours chosen can be changed according to each person and their understanding of each event

    data_clean.Time = rg.change(data_clean.Time, 'Afternoon', '16h00')

    data_clean.Time = rg.change(data_clean.Time, 'Dusk', '18h30')

    data_clean.Time = rg.change(data_clean.Time, 'Early morning', '07h30')

    data_clean.Time = rg.change(data_clean.Time, 'Early afternoon', '18h00')

    data_clean.Time = rg.change(data_clean.Time, 'Evening', '20h00')

    data_clean.Time = rg.change(data_clean.Time, 'Late afternoon', '19h30')

    data_clean.Time = rg.change(data_clean.Time, 'Midday', '12h00')

    data_clean.Time = rg.change(data_clean.Time, 'Midnight', '00h00')

    data_clean.Time = rg.change(data_clean.Time, 'Morning', '08h30')

    data_clean.Time = rg.change(data_clean.Time, 'Night', '21:30')

    #Next, we will change patterns to make all cohesive

    #Delete 5 characters that goes after '-' and a white space
    data_clean.Time = rg.change_re(data_clean.Time, r'(s\-\s\w{2}\w\w{2})', '') 

    #Delete white spaces at the beggining
    data_clean.Time = rg.change_re(data_clean.Time, r'\s*', '')

    #Delete white spaces at the end
    data_clean.Time = rg.change_re(data_clean.Time, r'\s$', '')

    #Delete 5 characters after '/' and a white space
    data_clean.Time = rg.change_re(data_clean.Time, r'(\/\s\w{5})', '')

    #Delete 5 characters that go after '-' (could have combine it with the former)
    data_clean.Time = rg.change_re(data_clean.Time, r'(\-\w{2}\w\w{2})', '')

    #Delete a white space, 2 characters, white space, 5 characters
    data_clean.Time = rg.change_re(data_clean.Time,r'( \w{2} \w{5})', '')

    #Delete 5 characters after '/' followed by white space
    data_clean.Time = rg.change_re(data_clean.Time, r'(\/\s\w{5})', '')

    #Delete 4 characters after a ',' or a character after a ','
    data_clean.Time = rg.change_re(data_clean.Time, r'(\,\s\w{4})', '')

    data_clean.Time = rg.change_re(data_clean.Time, r'\,\w', '')

    #Delete any character in braquets following a withe space
    data_clean.Time = rg.change_re(data_clean.Time, r'(\s\(\w*\))', '')

    #Delete any character in braquets following a '\'
    data_clean.Time = rg.change_re(data_clean.Time,r'(\(\w*\))', '')

    #Delete combination of '-' followed by white space and characters
    data_clean.Time = rg.change_re(data_clean.Time,r'( \-\w*\s\w*\s\w*\s\w*)', '')

    #Delete any two lowercase followed by any character
    data_clean.Time = rg.change_re(data_clean.Time,r'[a-z]{2}\w*', '')

    #Delete any character following a '/'
    data_clean.Time = rg.change_re(data_clean.Time,r'(\/\w*)', '')

    #Deletion of special characters and the beggining or the end
    data_clean.Time = rg.change_re(data_clean.Time,r'(\<*)', '')

    data_clean.Time = rg.change_re(data_clean.Time,r'(\>*)', '')

    data_clean.Time = rg.change_re(data_clean.Time,r'(\?$)', '')

    #Finally, we just have to change certain hour formats
    data_clean.Time = rg.change(data_clean.Time,'13h345', '13h45')

    data_clean.Time = rg.change(data_clean.Time, '15h00j', '15h00')

    data_clean.Time = rg.change(data_clean.Time, '0830', '08h30')

    data_clean.Time = rg.change(data_clean.Time, '11h115', '11h15')

    data_clean.Time = rg.change(data_clean.Time, '1500', '15h00')

    data_clean.Time = rg.change(data_clean.Time, '06j00', '06h00')

    #The last touch will be to change the 'h' for ':'

    data_clean.Time = rg.change_re(data_clean.Time,r'[a-z]', ':')

#4. 'Activity'

    #We just want the main categories, so we don't any any additional information
    #The first step is to delete such information
    #This code deletes every character after a white space
    data_clean.Activity = rg.change_re(data_clean.Activity, r'\s(\w*\s)*\w*', '')

    #Delete braquets with characters inside after the first word
    data_clean.Activity = rg.change_re(data_clean.Activity, r'(\-\w*)+', '')

    #Delete all non-word characters
    data_clean.Activity = rg.change_re(data_clean.Activity, r'\W+', '')

    #After this first check, certaing subcategories were found, so we changed them to a main category
    data_clean.Activity = rg.change(data_clean.Activity, 'Surf', 'Surfing')

    data_clean.Activity = rg.change(data_clean.Activity, 'Body', 'Surfing')

    data_clean.Activity = rg.change(data_clean.Activity, 'Surfinging', 'Surfing')

    data_clean.Activity = rg.change(data_clean.Activity, 'Surfingsittin', 'Surfing')

    data_clean.Activity = rg.change(data_clean.Activity, 'Windsurfing', 'Surfing')

    data_clean.Activity = rg.change(data_clean.Activity, 'Paddling', 'Surfing')

    data_clean.Activity = rg.change(data_clean.Activity, 'Paddle', 'Surfing')

    data_clean.Activity = rg.change(data_clean.Activity, 'Kayak', 'Kayaking')

    data_clean.Activity = rg.change(data_clean.Activity, 'Kayakinging', 'Kayaking')

    data_clean.Activity = rg.change(data_clean.Activity, 'Freedom', 'Swimming')

    data_clean.Activity = rg.change(data_clean.Activity, 'Scuba', 'Diving')

    data_clean.Activity = rg.change(data_clean.Activity, 'Dived', 'Diving')

    data_clean.Activity = rg.change(data_clean.Activity, 'Divingsubmerged', 'Diving')

    data_clean.Activity = rg.change(data_clean.Activity, 'Divingdiving', 'Diving')

    data_clean.Activity = rg.change(data_clean.Activity, 'Pearl', 'Diving')

    data_clean.Activity = rg.change(data_clean.Activity, 'Free', 'Diving')

    data_clean.Activity = rg.change(data_clean.Activity, 'FLoating', 'Bathing')

    data_clean.Activity = rg.change(data_clean.Activity, 'boat', 'Boating')

    data_clean.Activity = rg.change(data_clean.Activity, 'Boat', 'Boating')

    data_clean.Activity = rg.change(data_clean.Activity, 'Boatinging', 'Boating')

    data_clean.Activity = rg.change(data_clean.Activity, 'Sailing', 'Boating')

#5. 'Sex'

    #In this case, it is only necessary to change a few characters
    #It is important to point out that the way we refer to the colums is different

    data_clean["Sex "] = rg.change(data_clean["Sex "], 'N', 'M')

    
    data_clean["Sex "] = rg.change(data_clean["Sex "], 'lli', 'Unknown')

    
    data_clean["Sex "] = rg.change(data_clean["Sex "], '.', 'Unknown')


#6. 'Fatal (Y/N)

    #Same process as 'Sex'

    
    data_clean["Fatal (Y/N)"] = rg.change(data_clean["Fatal (Y/N)"], 'M', 'N')

    data_clean["Fatal (Y/N)"] = rg.change(data_clean["Fatal (Y/N)"], 'y', 'Y')

    data_clean["Fatal (Y/N)"] = rg.change(data_clean["Fatal (Y/N)"], '2017', 'Unknown')

    data_clean["Fatal (Y/N)"] = rg.change(data_clean["Fatal (Y/N)"], 'UNKNOWN', 'Unknown')

    data_clean["Fatal (Y/N)"] = rg.change_re(data_clean["Fatal (Y/N)"], r'\s*', '')

#7 'Case Number'

    #There are three columns that may seem to have the same values:
    #'Case Numner', 'Case Number.1' and 'Case Numer.2'

    #However, if we check it, we will see it is False

    rg.equal(data_clean["Case Number"], data_clean["Case Number.1"])

    rg.equal(data_clean["Case Number"], data_clean["Case Number.2"])

    rg.equal(data_clean["Case Number.1"], data_clean["Case Number.2"])

    #This could be a problem, but as there just a few cases, we can use only 'Case Number'

    data_clean = data_clean .drop(["Case Number.1", "Case Number.2"], axis = 1)

    #Now, we have to check the observations and correct possible errors

    #Delete fragment that come after the last '.'
    data_clean["Case Number"] = rg.change_re(data_clean["Case Number"], r'(\.\w$)', '')

    #Delete combination of uppercase and number after '.'
    data_clean["Case Number"] = rg.change_re(data_clean["Case Number"], r'\.[A-Z]\w', '')

    #Delete combination of upper and lowercase that comes after '.'
    data_clean["Case Number"] = rg.change_re(data_clean["Case Number"], r'\.[A-Z]|[a-z]', '')

    #Delete last '.'
    data_clean["Case Number"] = rg.change_re(data_clean["Case Number"],  r'\.$', '')

    #Delete '/'
    data_clean["Case Number"] = rg.change_re(data_clean["Case Number"],  r'\/$', '')

    #Delete combination of '.' and '&'
    data_clean["Case Number"] = rg.change_re(data_clean["Case Number"],  r'\.\ \&', '')

    #Delete combination of '.' or '-' and 0-1 letter after
    data_clean["Case Number"] = rg.change_re(data_clean["Case Number"],  r'(\.|-)\w?$', '')

#Once we have the clean dataframe we export it as a .csv file

data_clean.to_csv(r'C:\Users\juanp\Ironhack\pandas-project\data\data_clean.csv' , index = True)