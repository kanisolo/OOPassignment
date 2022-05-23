# -*- coding: utf-8 -*-
"""
Prescription

"""

class Prescription:
    def __init__(self,quantity,dosage):
        self.quantity = quantity
        self.dosage = dosage
        
    def __str__(self):
        return 'String'


presc1 = Prescription(10, 2)
print(presc1)