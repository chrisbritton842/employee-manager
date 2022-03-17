from employee import Employee


class Manager (Employee):
    def __init__(self, name, title, salary, manager=None):
        super().__init__(name, title, salary, manager)
        self.employees=[]

    def add_employee(self, employee):
        self.employees.append(employee)
    def __repr__(self):
        return f'Manager("{self.name}", "{self.title}", "{self.salary}", "{self.manager}", "{self.employees}")'

    def get_manager_bonus(self, multiplier):
        salaries = [self.salary]
        if self.employees:
            for employee in self.employees:
                salaries.append(employee.salary)
                
            return sum(salaries)*multiplier
# annie = Manager('Annie', 100000, 'Director')
# alvy = Employee('Alvy', 75000, 'Analyst', annie)
# print(repr(annie))
# print(repr(alvy))
hobbes = Manager("Hobbes", "Founder", 1000000)
calvin = Manager("Calvin", "Director", 130000, hobbes)
susie = Manager("Susie", "TA Manager", 100000, calvin)
lily = Employee("Lily", "TA", 90000, susie)
clifford = Employee("Clifford", "TA", 90000, susie)
print(hobbes.get_manager_bonus(0.05))
