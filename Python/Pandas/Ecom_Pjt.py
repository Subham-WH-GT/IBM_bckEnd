import pandas as pd

data=pd.read_csv('C:\\Users\\user\\Desktop\\IBM_bckEnd\\eDataset.csv')

#Query1: Print the data of the 1st 10 Rows . . .
print(data.head(10))

#Query2: Print the data of the Last 10 Rows . . .
print(data.tail(10))

#Query3: Check Datatype of each colummn . . .
print(data.dtypes)

#Query4: Count total Rows and Columns in the Dataset . . .
print('Total Columns Present is:',len(data.columns))
print('Total Rows Present is:',len(data))

#query5: Find maximum and minimum ratings . . .
#First convert the dtype of ratings column to numeric values from object type
data['ratings']=pd.to_numeric(data['ratings'],errors='coerce')
print(data['ratings'].dtype) #Output: float
#Now apply min and max to find the result
print(data['ratings'].max()) #gives max price
print(data['ratings'].min())

#Query6: Find the average ratings
print(data['ratings'].mean())

#Query6: count of total numbers of OnePlus models
redmi_mi_count=data['name'].str.contains('OnePlus',case=False).sum() #to make case insensitive
print(redmi_mi_count)

#Query7: Find number of ratings of the following model : Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)
print(data[data['name']=='Apple 20W USB-C Power Adapter (for iPhone, iPad & AirPods)']['no_of_ratings'])

#Query8: how many people is having oneplus model with ratings greater or equal 4.5 . . .
required_rows=data[(data['name'].str.contains('OnePlus',case=False)) & (data['ratings']>=4.5)]
final_rows=required_rows.shape[0]
print(final_rows)
#Second way to print the length of the extracted dataframe
print(len(data[(data['name'].str.contains('OnePlus',case=False)) & (data['ratings']>=4.5)]))
print((data[(data['name'].str.contains('OnePlus',case=False)) & (data['ratings']>=4.5)]).count())

#Query9: Print the link of the product with name : boAt BassHeads 100 in-Ear Wired Headphones with Mic (Black)
print(data[data['name']=='boAt BassHeads 100 in-Ear Wired Headphones with Mic (Black)']['link'])

