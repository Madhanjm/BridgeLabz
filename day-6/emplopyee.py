class Employee:
    def __init__(self,emp_id,emp_name,salary):
        self.emp_id=emp_id
        self.emp_name=emp_name
        self.__salary=salary
        
    def cal_bonus(self):
        return self.__salary*0.10
    
    def get_sal(self):
        return self.__salary
    
    def update_sal(self,amount):
        if amount<=0:
            raise ValueError("Not a valid salary")
        self.__salary=amount
        
class Manager(Employee):
    
    def cal_bonus(self):
        return self.__salary*0.20
        