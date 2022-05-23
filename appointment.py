# -*- coding: utf-8 -*-
"""
Appointment & appointment schedule classes
The two clases have a compoosite relationship

"""

import patient
import receptionist


class Appointment:
    '''
    Has an aggregate relationship with the patient
    Receives appointment from patient
    '''
    def __init__(self,patient):
        #self.appointment_type = appointment_type
        self.obj_patient = patient
    




class AppointmentSchedule:
    '''
    Appointment schedule has an aggreate relationship with Appointment
    create a class attribute to store appointment details as tuples
    '''
    
    appointments = []
    
    
    def __init__(self,appointment):
        self.appointment = Appointment(patient)

    

    def add_appointmnet(self):
        #appointment would be added by a receptionist
        pass

              
    def cancel_appointment(self):
        #appointment should be cancelled by a receptionist
        pass

                 
    def find_next_available(self):
        #
        pass
    


