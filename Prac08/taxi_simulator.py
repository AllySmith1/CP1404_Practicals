from Prac08.taxi import Taxi
from Prac08.taxi import SilverServiceTaxi

def main():
    taxi = ''
    bill_total = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's drive!")

    choice = show_menu()

    while choice.lower() != 'q':
        if choice.lower() == 'c':
            taxi = handle_choose(taxis, bill_total)
            choice = show_menu()
        elif choice.lower() == 'd':
            handle_drive(taxi, bill_total)
            choice = show_menu()
        else:
            print('Invalid Menu Option')
            choice = show_menu()
    handle_quit(taxi, taxis, bill_total)


def list_taxis(taxis):
    for i in range(len(taxis)):
        print('{} - {}'.format(i, taxis[i]))


def handle_choose(taxis, bill_total):
    print('Taxis available:')
    list_taxis(taxis)
    choice = int(input('Choose taxi: '))
    taxi = taxis[choice]

    bill_total = update_bill(taxi, bill_total)
    print('Bill to date:  ${:.2f}'.format(bill_total))
    return taxi


def update_bill(taxi, bill_total):
    bill_total += taxi.get_fare()
    return bill_total


def handle_drive(taxi, bill_total):
    distance = int(input("Drive how far? "))
    taxi.start_fare()
    taxi.drive(distance)
    print('Your {} tripe cost you ${:.2f}'.format(taxi.name, taxi.get_fare))
    bill_total = update_bill(taxi, bill_total)
    print('Bill to date: ${:.2f}'.format(bill_total))


def show_menu():
    menu = 'q)uit, c)hoose, d)rive'
    print(menu)
    choice = input('>>> ')
    return choice


def handle_quit(taxi, taxis, bill_total):
    print('Total trip cost: ${:.2f}'.format(bill_total))
    print('Taxis are now: ')
    list_taxis(taxis)

if __name__ == '__main__':
    main()