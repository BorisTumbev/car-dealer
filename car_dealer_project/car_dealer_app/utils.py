#from enum import Enum
import datetime


curr_year = datetime.datetime.now().year


conditions         = (('N','New'),
                      ('U','Used'))

transmission_types = (('A','Auto'),
                      ('M','Manual'),
                      ('S','Semi-auto')) 

engine_types       = (('D','Disel'),
                      ('P','Petrol'),
                      ('E','Electric'),
                      ('H','Hybrid'))

vehicle_types      = (('A','Automobile'),
                     ('M','Motorcycle'),
                     ('B','Bus'),
                     ('T','Truck'))

sell_status        =(('A','Active'),
                     ('S','Sold'),
                     ('P','Pending'),
                     ('D','Declined')


)

# class Conditions(Enum):
#     New  = 'New'
#     Used = 'Used'

# class TransmissionTypes(Enum):
#     Auto      = 'Auto'
#     Manual    = 'Manual'
#     Semi_auto = 'Semi-auto'

# class EngineTypes(Enum):
#     Diesl    = 'Disel'
#     Petrol   = 'Petrol'
#     Electric = 'Electric'
#     Hybrid   = 'Hybrid'

# class VehicleTypes(Enum):
#     Automobile = 'Automobile'
#     Motorcycle = 'Motorcycle'
#     Bus        = 'Bus'
#     Truck      = 'Truck'

