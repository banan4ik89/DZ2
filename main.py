class Employee:
    def __init__(self, name, position, salary):
        
        self.name = name
        self.position = position
        self.salary = salary

    def get_salary_info(self):
        
        return f"Заробітна плата {self.name}: {self.salary}"


if __name__ == "__main__":
    employee = Employee("Іван", "Програміст", 30000)
    print(employee.get_salary_info())
