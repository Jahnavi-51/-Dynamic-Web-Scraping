import pandas as pd
student ={
    "Name":['janu','vasu','ravi','gopi','gokul','golu','om'],
    "Age":[22,19,23,22,22,25,24],
    "City":['vj','vj','vs','bh','tn','pd','od'],
    "Salary":[20000,22000,77000,65430,76580,46573,89050]
}

df = pd.DataFrame(student)
print(df)

n = df.loc[3,'Name']
print(n)

avg = df ['Age'].mean()
print(round(avg))

high = df ['Salary'].max()
print(high)

higher = df[df['Salary']>70000]
print(higher)

df['Experience'] = [2,3,1,2,0.6,2,1]
print("\n",df)

gh = df.groupby('City')['Salary'].mean()
print(gh)

rank =[24,56,86,87,90,89,76]
rk= pd.Series(rank)
print(rk)

jh = pd.read_csv('C:/Users/LENOVO/Documents/data.csv', sep=",", error_bad_lines=False)

print(jh.head())