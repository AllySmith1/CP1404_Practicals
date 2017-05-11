from Prac07.guitar import Guitar

# test get_age method

g1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
g2 = Guitar("Guitar 2", 2011, 1500.50)

print("get_age() - Expected 94. Got", Guitar.get_age(g1))
print("get_age() - Expected 5. Got", Guitar.get_age(g2))

print("is_vintage() - Expected True. Got", Guitar.is_vintage(g1))
print("is_vintage() - Expected False. Got", Guitar.is_vintage(g2))
