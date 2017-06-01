from Prac08.taxi import Taxi
from Prac08.taxi import UnreliableCar
from Prac08.taxi import SilverServiceTaxi

# Test Taxi Class
prius = Taxi('Prius 1', 100)
prius.drive(40)
print(prius)
print(prius.get_fare())

prius.start_fare()
prius.drive(100)
print(prius)
print(prius.get_fare())
print()

# Test Unreliable Car Class
ford = UnreliableCar('Ford', 100, 50)
ford.drive(40)
print(ford)
print()

# Test Silver Service Taxi Class
hummer = SilverServiceTaxi('Hummer', 200, 2)
hummer.drive(10)
print(hummer)
print('${:.2f}'.format(hummer.get_fare()))