employees = []


def add_employee(name):
    print("Adding employee:[ ", name, " ] into employee data base")
    employees.append(name)


def remove_employee(name):
    print("removing employee:[ ", name, " ] into employee data base")
    employees.remove(name)


def print_employees():
    print(employees)
