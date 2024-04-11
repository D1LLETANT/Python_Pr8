import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("products.csv")

def function(data):
    data = int(data)
    return data
df['Stock Quantity'] = df['Stock Quantity'].apply(function)

temp=df.pivot_table(index='Category', aggfunc='count',values='Stock Quantity')

temp.plot(kind = "pie",subplots=True)
plt.show()