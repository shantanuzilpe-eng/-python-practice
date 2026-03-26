import pandas as pd

# Read Excel file
df = pd.read_excel("employee.xlsx")

# a) Employees in Automotive domain
print("Employees in Automotive domain:")
auto_emp = df[df['Department'] == 'Automotive']
print(auto_emp)

# b) Details of employee by ID
emp_id = int(input("Enter Employee ID: "))
emp_details = df[df['Employee ID'] == emp_id]
print("\nEmployee Details:")
print(emp_details)

# c) List of Developers
print("\nList of Developers:")
developers = df[df['Designation'] == 'Developer']
print(developers)
