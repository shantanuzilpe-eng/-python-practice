import pandas as pd
import matplotlib.pyplot as plt

# Load dataset (make sure CSV file is in same folder)
data = pd.read_csv("sales_data.csv")

# a) Total profit line plot
plt.figure()
plt.plot(data['month_number'], data['total_profit'], marker='o')
plt.title("Total Profit of All Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid()
plt.show()

# b) Multiline plot for all products
plt.figure()
plt.plot(data['month_number'], data['facecream'], label='Face Cream')
plt.plot(data['month_number'], data['facewash'], label='Face Wash')
plt.plot(data['month_number'], data['toothpaste'], label='Toothpaste')
plt.plot(data['month_number'], data['bathingsoap'], label='Bathing Soap')
plt.plot(data['month_number'], data['shampoo'], label='Shampoo')
plt.plot(data['month_number'], data['moisturizer'], label='Moisturizer')

plt.title("Sales Data of All Products")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# c) Bar chart for face cream & face wash
plt.figure()
plt.bar(data['month_number'], data['facecream'], label='Face Cream')
plt.bar(data['month_number'], data['facewash'], bottom=data['facecream'], label='Face Wash')

plt.title("Face Cream & Face Wash Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.legend()
plt.show()

# d) Pie chart for total sales of each product
total_sales = [
    data['facecream'].sum(),
    data['facewash'].sum(),
    data['toothpaste'].sum(),
    data['bathingsoap'].sum(),
    data['shampoo'].sum(),
    data['moisturizer'].sum()
]

labels = ['Face Cream', 'Face Wash', 'Toothpaste', 'Bathing Soap', 'Shampoo', 'Moisturizer']

plt.figure()
plt.pie(total_sales, labels=labels, autopct='%1.1f%%')
plt.title("Total Sales Distribution")
plt.show()
