i = 1
employees = []
1
class EmpleyadoAko:
    def __init__(self, name, department, position, rate):
        self.name = name
        self.department = department
        self.position = position
        self.rate = rate
    def getsalary(self, hourly):
        return self.rate * hourly

while i == 1:
    print("[1] Add New Employee")
    print("[2] Enter Hourly of Employee")
    print("[3] Show Employee")
    print("[4] Exit")
    str = input("Enter option: ")
    if str == "1":
        a = (input("enter name: "))
        employees.append(a)
        b = (input("enter department: "))
        employees.append(b)
        c = (input("enter position: "))
        employees.append(c)
        d = (int(input("enter rate: ")))
        employees.append(d)
    elif str =="2":
        Object = EmpleyadoAko(a, b, c, d)
        e = (int(input("Employee number: ")))
        print(employees[e])
        f = (int(input("enter hourly: ")))
        print(Object.getsalary(f))
        employees.append(f)
    elif str =="3":
        print("""Employee Number: {}
  		Employee Name: {}
  		Employee Department: {}
  		Employee Position: {}
  		Employee Rate: {}""".format(e, a, b, c, d)) 			 
    elif str == "4":
        exit(1)
    else:
        print("invalid input")
