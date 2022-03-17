class Employee:
    def __init__(self, name, title, salary, manager=None):
        self.name=name
        self.title=title
        self.salary=salary
        self.manager=manager
        if manager:
            manager.add_employee(self)
    # @property
    # def salary(self):
    #     return self.salary
    def __repr__(self):
        return f'Manager("{self.name}", "{self.title}", "{self.salary}", "{self.manager}")'

    def get_bonus(self, multiplier):


        return salary*multiplier

    # def bonus(self):
    #     salaries = [self.salary]
    #     if self.employees:
    #         for employee in self.employees:
    #             salaries.append(employee.salary)
    #         return employee.bonus = sum(salaries)*0.05
    #     else:
    #         return self.bonus = salary*0.05
