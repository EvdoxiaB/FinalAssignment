#Import packages
import pandas as pd

#Import data as csv
df = pd.read_csv(r'C:\Users\eudox\Desktop\Workearly\Python\Final_Assignment\Export_Data.csv')

print(df)
print(df.info())

#Groupby data per suitable columns and aggregate per sum of bottles_sold
bottles_sold_per_item = df.groupby(['zip_code', 'store_name', 'item_description']).agg({'bottles_sold': 'sum'}).sort_values(by=['zip_code', 'bottles_sold'],
                                                             ascending=[True, False])

#Export to csv in orde to upload the result in Tableau Public
df2 = pd.DataFrame(bottles_sold_per_item)
df2.rename(columns={'bottles_sold': 'bottles_sold_item'}, inplace=True)
df2.to_csv(r'C:\Users\eudox\Desktop\Workearly\Python\Final_Assignment\ItemSales.csv')