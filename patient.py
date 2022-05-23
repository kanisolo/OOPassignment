"""
Patient class

"""
import appointment

class Patient():

    def __init__(self,name,address,phone):
        self.name = name
        self.address = address
        self.phone = phone
        self.request = (self.name, self.address,self.phone)
    
    def request_repeat(self):
        pass
    
    def request_appointment(self):
        #patient needs to make a request for an appointment through the receptionist receptionist
        return appointment.receptionist.Receptionist.make_appointment(self.request)
        





#patient1 = Patient('chris', 'ntinda', 545454)
#print(patient1.request_appointment())
#print(patient1.request_appointment())
#print(appointment.receptionist.make_appointment())
#appointment.receptionist.make_appointment(request)
#print(patient1.request_appointment())

