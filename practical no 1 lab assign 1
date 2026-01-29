class Employee:
    def __init__(self, name, emp_id, department, basic_salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.basic_salary = basic_salary

    def calculate_salary(self):
        self.da = 0.92 * self.basic_salary
        self.hra = 0.58 * self.basic_salary
        self.ta = 0.30 * self.basic_salary

        self.gross_salary = self.basic_salary + self.da + self.hra + self.ta
        self.net_salary = self.gross_salary - 500   # LIC deduction

    def display(self):
        print("Employee Name   :", self.name)
        print("Employee ID     :", self.emp_id)
        print("Department      :", self.department)
        print("Basic Salary    :", self.basic_salary)
        print("DA              :", self.da)
        print("HRA             :", self.hra)
        print("TA              :", self.ta)
        print("Gross Salary    :", self.gross_salary)
        print("LIC Deduction   : 500")
        print("Net Salary      :", self.net_salary)


# Main Program
e = Employee("Trisha", 101, "IT", 30000)
e.calculate_salary()
e.display()
