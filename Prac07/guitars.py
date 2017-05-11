from Prac07.guitar import Guitar

print("My Guitars!")
guitars = []
valid_input = True

while valid_input is True:
    name_input = input("Name: ")
    if name_input == "":
        print("...snip...")
        valid_input = False
    else:
        year_input = int(input("Year: "))
        cost_input = float(input("Cost: $"))
        guitars.append(Guitar(name_input, year_input, cost_input))
        print(guitars[-1], "added.")

print("These are my guitars:")
for i in range(len(guitars)):
    if guitars[i].is_vintage() is True:
        vintage_string = "(vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i + 1, guitars[i].name, guitars[i].year, guitars[i].cost, vintage_string))