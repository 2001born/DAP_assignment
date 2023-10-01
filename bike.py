import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("bike\europe-motorbikes-zenrows.csv")
data=pd.DataFrame(df)
print(data.iloc[:,1])

name = list(data.iloc[:5,3])
price = list(data.iloc[:5,0])


# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(name,price, color='blue')

# Add title and labels
plt.title('Bikes and their prices')
plt.xlabel('Bike name')
plt.ylabel('Price')

# Show the bar chart
plt.show()