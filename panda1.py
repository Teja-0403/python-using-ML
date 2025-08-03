import pandas as pd
data={
    'Name':['Teja','Gopi','Padma'],
    'Age':[20,19,32],
    'City':['Vinukonda','Guntur','Hyderabad']
}
df=pd.DataFrame(data)#input the data in the rows and columns
print(df)#printing the data
print(df['Name'])#printing the name column
print(df[['Name','Age']])#prints name and age column
print(df.iloc[0])#indexing 0
print(df.iloc[1,1])#indexing row 1,column 1
data={
    'Name':['Teja','Gopi','Padma'],
    'Age':[20,None,32],
    'City':[None,'Guntur','Hyderabad']
}
df=pd.DataFrame(data)#accesing the new data
print(df)
print(df.isnull())
print(df.isnull().sum())
df.fillna(1,inplace=True)#filling the places null if 1
print(df)
print(df.isnull())#checking whether it is null
print(df.isnull().sum())#check and suming
data={
    'Name':['Teja','Gopi','Padma'],
    'Age':[20,19,None],
    'City':['Vinukonda',None,'Hyderabad']
}
df=pd.DataFrame(data)
print(df)
df.dropna(inplace=True)#Prints the true at none
print(df)
data={
    'Name':['Prassu','Akshaya','Vaishu'],
    'Age':[19,19,19],
    'City':['Guntur','Vijayawada','Narasaraopet']
}
df=pd.DataFrame(data)
print(df)
df.rename(columns={'Name': 'Full Name'},inplace=True)
df.rename(columns={'Age':'Years','City':'Location'},inplace=True)
print(df)