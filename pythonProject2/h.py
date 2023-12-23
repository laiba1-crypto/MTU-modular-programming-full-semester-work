def mainmenu():
    banner = 'LONG ISLAND HOLIDAYS'
    print(banner)
    print('=' * len(banner))
    print(f'1. Make a Booking' + '\n' + '2. Review Bookings' + '\n' + '3. Exit')

def loop_menu(accommodation_type, accommodation_bookings, extras_list):
    booking_count = 0
    while True:
        try:
            mainmenu()
            option = int(input('Enter 1, 2, or 3: '))
            while option != 3:
                if option ==1:
                    print('Make a Booking')
                    for i in range(30):
                        option_one(accommodation_bookings, extras_list)
                        break
                    booking_count= booking_count + 1
                    print(f'you have {booking_count} bookings and {30 - booking_count} bookings available. ')
                    display_booking_details(booking_count, accommodation_type)
                elif option ==2:
                    print('Review Bookings')
                    option_two()
                else:
                    print('Exit')
        except ValueError:
            print('Invalid')

def option_one(accommodation_bookings, extras_list):
    while True:
        try:
            Surname = str(input('Enter your Surname: '))
            if 1 < len(Surname) <= 14:
                break
            else:
                print('Surname must be between 1-14 characters')
                continue
        except ValueError:
            print('Invalid input')
            continue
    while True:
        try:
            phone_num = int(input('Enter your phone number: '))
            if 1 < len(phone_num) <=12:
                break
            else:
                print('phone number must be less than 12 digits')
                continue
        except ValueError:
            print('Invalid input')
            continue
    while True:
        print('1. Deluxe Caravan, 2. Standard Caravan, 3. Camp')
        print('Please choose 1, 2, 3: ')
        try:
            accommodation_type = int(input('Enter the accommodation type here:'))
            if accommodation_type ==1:
                print('Deluxe Caravan')
                break
            else:
                print('only choose between 1, 2, or 3')
                continue
        except ValueError:
            print('Invalid input')
    while True:
        try:
            num_of_guests = int(input('Enter number of guests:'))
            if 0 <= num_of_guests:
                while True:
                    try:
                        kids_club = int(input('Enter number of children who will be in kids club, if any: '))
                        if 0 <= kids_club < num_of_guests:
                            break
                        elif kids_club ==0:
                            print('Return to guest input')
                            break
                        else:
                            print('Invalid')
                            break
                    except ValueError:
                        print('Try to put the details again please!')
                while True:
                    try:
                        family_pool_pass = str(input('Do you want to buy a family pool pass? y/n:'))
                        if family_pool_pass == 'y' or 'Y':
                            break
                        elif family_pool_pass == 'n' or 'N':
                            break
                        else:
                            print('Invalid input')
                            continue
                    except ValueError:
                        print('Try to put the details again please!')
def booking_details(booking_count , accommodation_type):
    banner = 'Booking Details'
    print(banner)
    print('-' * len(banner))
    print(f'Booking ID: {booking_count}')
    print(f'Accommodation Type: {accommodation_type}')
    print(f'No. Of People: {num_of_guests}')
    print(f'Pool Pass: {family_pool_pass}')
    print(f' No. Of Kids Club: {kids_club}')
    print(f'Cost: {}euros.')

def main():
    mainmenu()
    accommodation_type, accommodation_bookings, extras_list = loop_menu()
    accommodation_bookings, extras_list = option_one()
    booking_count, accomodation_type = booking_details()


main()





