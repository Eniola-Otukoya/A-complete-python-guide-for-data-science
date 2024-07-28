# main.py
from vehicle_impl import Car, Motorcycle

vehicles = [Car(), Motorcycle()]

for vehicle in vehicles:
    print(vehicle.start_engine())