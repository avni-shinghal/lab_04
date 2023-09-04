class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id} {self.name} {self.age} {self.salary}"


def sort_employees(employees, sorting_parameter):
    if sorting_parameter == 1:  # Sort by Age
        return sorted(employees, key=lambda emp: emp.age)
    elif sorting_parameter == 2:  # Sort by Name
        return sorted(employees, key=lambda emp: emp.name)
    elif sorting_parameter == 3:  # Sort by Salary
        return sorted(employees, key=lambda emp: emp.salary)
    else:
        raise ValueError("Invalid sorting parameter")


def main():
    employees = [
        Employee("161E90", "Raman", 41, 56000),
        Employee("161F91", "Himadri", 38, 67500),
        Employee("161F99", "Jaya", 51, 82100),
        Employee("171E20", "Tejas", 30, 55000),
        Employee("171G30", "Ajay", 45, 44000),
    ]

    print("Choose sorting parameter:")
    print("1. Age")
    print("2. Name")
    print("3. Salary")

    try:
        sorting_parameter = int(input("Enter your choice: "))
        sorted_employees = sort_employees(employees, sorting_parameter)
        print("Sorted Employee Table:")
        for emp in sorted_employees:
            print(emp)
    except ValueError:
        print("Invalid choice. Please enter a valid sorting parameter.")


if __name__ == "__main__":
    main()
