from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar

# Test Taxi Class
prius1 = Taxi('Prius 1', 100)
prius1.drive(40)
print(prius1)
print(prius1.get_fare())

prius1.start_fare()
prius1.drive(100)
print(prius1)
print(prius1.get_fare())
print()

# Test Unreliable Car Class
ford = UnreliableCar('Ford', 100, 50)
ford.drive(40)
print(ford)
print()