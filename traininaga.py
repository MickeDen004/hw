class Employee:

    @staticmethod
    def sample(x):
        print('Inside static method', x)

# call static method

Employee.sample(10)

# can be called using object
emp = Employee()
emp.sample(10)

class Employee_2():

    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == "DreamApp Beta Version":
            requirements = ['task_1', 'task_2', "task_3"]
        else:
            requirements = ['task_1']
        return requirements

    # instance method
    def work(self):
        # call static method from instance method
        requirements = self.gather_requirement(self.project_name)
        for task in requirements:
            print("Completed", task)

emp = Employee_2('Kelly', 12000, "James Doe Holdings")
emp.work()
emp_2 = Employee_2('Howard', 12300, "DreamApp Beta Version")
emp_2.work()
