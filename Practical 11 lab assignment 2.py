import matplotlib.pyplot as plt

# Sample data (you can modify values)
companies = ['Microsoft', 'Google', 'Amazon', 'IBM', 'Deloitte', 'Capgemini', 'ATOS', 'Amdocs']
recruitments = [120, 150, 180, 90, 110, 130, 80, 95]

# a) Bar Chart
plt.figure()
plt.bar(companies, recruitments)
plt.title("Company Recruitment Data")
plt.xlabel("Companies")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=30)
plt.show()

# b) Pie Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
plt.title("Recruitment Distribution")
plt.show()

# c) Customized Pie Chart
plt.figure()
explode = [0, 0.1, 0, 0, 0, 0, 0, 0]  # Highlight Google
plt.pie(recruitments, labels=companies, autopct='%1.1f%%', explode=explode)
plt.title("Customized Pie Chart")
plt.show()

# d) Doughnut Chart
plt.figure()
plt.pie(recruitments, labels=companies, autopct='%1.1f%%')
centre_circle = plt.Circle((0, 0), 0.70, fc='white')
fig = plt.gcf()
fig.gca().add_artist(centre_circle)
plt.title("Doughnut Chart")
plt.show()

# e) Comparison (IBM vs Amdocs)
plt.figure()
comp = ['IBM', 'Amdocs']
values = [90, 95]

plt.bar(comp, values)
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.ylabel("Recruitments")
plt.show()
