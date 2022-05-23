# -*- coding: utf-8 -*-
"""
Main
"""
import patient, appointment, receptionist

#Patient gives details to receptionist
patient = patient.Patient('solo', 'mbalwa', 545454)


# patient requests receptionist  to make appointment 

print(patient.request_appointment())

#Receptionist makes the appointment

print(patient.request)


if __name__== '__main__':
    pass

