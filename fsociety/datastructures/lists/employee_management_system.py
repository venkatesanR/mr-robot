import employee_database as emp_db

if __name__ == '__main__':
    print("Welcome to employee data base management")
    size = int(input("How many number of employees you want to insert:"))
    for i in range(0, size):
        print("Enter employee: ", i, "name to add: ")
        emp_db.add_employee(input())
    emp_db.employees.sort()
    emp_db.print_employees()
