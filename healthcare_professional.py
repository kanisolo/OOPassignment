# -*- coding: utf-8 -*-
"""
Health Care Professional

"""

class HealthCareProfessional:
    def __init__(self,name,employee_number):
        self.name = name
        self.employee_number = employee_number
        
    def consultation(self):
        pass
    
    

class Doctor(HealthCareProfessional):
    #HealthCareProfessional.__init__(self, name, employee_number):
    def issue_prescription(self):
        pass
    
class Nurse(HealthCareProfessional):
    pass
        

