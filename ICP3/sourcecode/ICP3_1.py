# Function for average salary
def avg_salary():
    print("Total salary of all employees = ", Employee.total_salary)
    print("Total number of employees = ", Employee.no_of_employees)
    return Employee.total_salary / Employee.no_of_employees

# Employee class 'Parent Class'
class Employee:
    no_of_employees = 0   # data member to count the number of Employees
    total_salary = 0     # data member to save the total salary


    # constructor to initialize name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.no_of_employees += 1
        Employee.total_salary += self.salary

    # Function to print employee details
    def get_employee_details(self):
        print("Name = ", self.name)
        print("Family =", self.family)
        print("Salary =", self.salary)
        print("Department =", self.department)

# Adding 3 employees
a = Employee("Edward", 7, 8000, "Management")
b = Employee("Bella", 3, 4000, "Audit")
c = Employee("Alice", 3, 12000, "Research")
print("Average salary = ", avg_salary())


#Inheriting parent class Employee to child class FullTimeEmployee
class FullTimeEmployee(Employee):
    def __init__(self, name, family, salary, department):
        Employee.__init__(self, name, family, salary, department)

    def get_fulltimeemployee_details(self):
        print("Name = ", self.name)
        print("Family =", self.family)
        print("Salary = ", self.salary)
        print("Department =", self.department)


d = FullTimeEmployee("Jacob", 9, 6000, "Sales")     #Adding 4th employee
print("\nAccess from full time employee function")
d.get_fulltimeemployee_details()

print("\nAccessing from parent class Employee function ")
d.get_employee_details()