
data = pd.read_csv("C:\\Users\\juanp\\Ironhack\\pandas-project\\data\\attacks.csv", encoding='cp1252')


fc.null(data) 

data_clean = data.dropna(0, how = 'all')

data_clean = data_clean.drop(["Unnamed: 22", "Unnamed: 23", "Location", "Name", "Species ", "Investigator or Source", "pdf", "href", "href formula","Age", "Date"], axis = 1)


data_clean[["Case Number", "Type", "Country", "Area", "Activity", "Injury"
                         , "Case Number.1", "Case Number.2","Sex ", "Fatal (Y/N)"]] = data_clean[["Case Number", "Type", "Country", "Area", "Activity", "Injury"
                         , "Case Number.1", "Case Number.2","Sex ", "Fatal (Y/N)"]].fillna("Unknown") 


data_clean[["Time", "Year"]] = data_clean[["Time", "Year"]].fillna(method ='ffill')



time = data_clean.Time
country = data_clean.Country
activity = data_clean.Activity 
fatal = data_clean["Fatal (Y/N)"]
sex = data_clean["Sex "]


