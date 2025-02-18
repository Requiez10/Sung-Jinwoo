class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, percentage):
        "Increases the salary by a given percentage."
        if percentage > 0:
            raise_amount = self.salary * (percentage / 100)
            self.salary += raise_amount
            print(f"{self.name}'s salary increased by {percentage}% (₱{raise_amount}). New salary: ₱{self.salary:.2f}\n")
        else:
            print("Raise percentage must be positive.")

    def display_employee(self):
        """Displays the employee's name, position, and salary with proper formatting."""
        print(f"Employee Name: {self.name}")
        print(f"Position: {self.position}")
        print(f"Salary: ₱{self.salary:,.2f}")

employee2 = Employee(name="Sung Jinwoo", position="Data Analyst", salary=75000)

employee2.give_raise(10)

employee2.display_employee()
