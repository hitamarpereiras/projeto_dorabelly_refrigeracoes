from . import mydatabase

class Cliente:
    def __init__(self, name, tell, email, address, problem, descri_problem, date_request, date_visit, service_condition, expenses, payment_condition):
        self.name = name
        self.tell = tell
        self.email = email
        self.address = address
        self.problem = problem
        self.descri_prom = descri_problem
        self.date_request = date_request
        self.date_visit = date_visit
        self.service_condition = service_condition
        self.expenses = expenses
        self.payment_condition = payment_condition