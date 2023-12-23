""""""
STUDENT ID: R00201303
NAME: LAIBA ASIF
PURPOSE: HOLIDAY CAMP PROJECT
""""""
import os.path as path

KIDS_CLUB = 100
POOL_PASS = 150

############################### reading data from files #########################################
def reading_bookings():
    file = open('Bookings_2022.txt', 'r')
    read = file.readlines()
    acc_type = []
    price = []
    numbers = []
    site=30
    for line in read:
        line_data = line.split(',')
        acc_type.append(line_data[0])
        price.append(int(line_data[1]))
        numbers.append(int(line_data[2]))

    return acc_type, price, numbers

def reading_extras():
    file = open('extras.txt', 'r')
    read = file.readlines()
    extras = []
    numbers = []
    for line in read:
        line_dta = line.split(',')
        extras.append(line_dta[0])
        numbers.append(int(line_dta[1]))
    return extras, numbers

############################# updating the files #########################################################
def save_bookings(acc_type, price, numbers):

    with open('Bookings_2022.txt', 'w') as file_data:
        for i, item in enumerate(acc_type):
            print((item + ',' + str(price[i]) + ',' + str(numbers[i])), file=file_data)


def save_extras(extras, numbers):
    with open('extras.txt', 'w') as file_data:
        for i, item in enumerate(extras):
            print((item + ',' + str(numbers[i])), file=file_data)

####################################### creating a booking ###############################################
def make_booking(acc_type, price, numbers, extras, extras_numbers):
    # call the function to make bookings
    
    banner = "LONG ISLAND HOLIDAYS - MAKE A BOOKING"
    print(banner)
    print("=" * len(banner))
    while True:
        try:
            family = input(f"Enter Family name: ")
            if 1 <= len(family) <= 15:
                break
            else:
                print(f'Family name must be between 1-15 characters')


        except ValueError:
            print('Invalid Input!')

    while True:
        try:
            phone = input(f"Enter Phone Number: ")
            if 1 <= len(phone) < 12:
                break
            else:
                print(f'phone number must be less than 12 digits')
        except ValueError:
            print('Invalid Input!')


    for i,item in enumerate(acc_type):
       print(f'{i+1}- {item} for {price[i]}' )

    user_choice = int(input())

    cost = 0
    price_booking = 0

    if user_choice == 1: # booking 1 (deluxe caravan)
        accommodation = acc_type[0]
        price_booking = price[0]
        numbers[0] += 1
     
    elif user_choice == 2: # booking 2 other caravan
        accommodation = acc_type[1]
        price_booking = price[1]
        numbers[1] += 1
 
    elif user_choice == 3: # camp
        accommodation = acc_type[2]
        price_booking = price[2]
        numbers[2] += 1

    else:
        print('NO Booking!')

    cost += price_booking
    

    while True:
        try:
            numbers_guests = int(input(f'Enter number of guests:'))
            break

        except ValueError:
            print('Invalid Input!')

    if numbers_guests > 1:
        while True:
            try:
                kids_club = int(input(f'Enter number of kids in kids club:'))
                if 0 <= kids_club < numbers_guests:
                    extras_numbers[0] += kids_club
                    break
                else:
                    print('number of kids in kids club must be less than number of guests')

            except ValueError:
                print('Invalid Input!')
    else:
        kids_club = 0



    pool_pass = input(f'Do you want a pool pass (y/n):')
    pool_pass = pool_pass.lower()

    if kids_club >= 1:
        cost += KIDS_CLUB * kids_club
        kids_club = str(kids_club)
    else:
        kids_club = 'none'

    if pool_pass == 'y':
        pool_pass = 'Yes'
        extras_numbers[1] += 1
        cost += POOL_PASS
    else:
        pool_pass = 'No'

    # save the files for booking and extra passing new values in lists
    save_bookings(acc_type, price, numbers)
    save_extras(extras, extras_numbers)

    exists = path.isfile("counter.txt")

    bookingid = 1

    if exists:
        with open("counter.txt", "r") as counter:
            bookingid = int(counter.read())
    else:
        with open("counter.txt", "w") as counter:
            print("1", file=counter)

    with open("counter.txt", "w") as counter:
        print(str(bookingid + 1), file=counter)

    if bookingid < 10:
        bookingid = "0" + str(bookingid)

    bookingid = str(bookingid)

    print("Booking Details")
    print('----------------')
    print("Name ", family)
    print(f"Accommodation Name:", acc_type[user_choice-1])
    print(f"Booking ID:", str(bookingid))
    print(f"Pool pass:", pool_pass)
    print(f"Number of people:", str(numbers_guests))
    print(f"Number of kids in kids club:", str(kids_club))
    print(f"Cost:", str(cost))
    


    with open(family + "_" + bookingid + ".txt", "w") as bookingfile:
        print("== Booking Details ==", file=bookingfile)
        print("Name ", family,file=bookingfile)
        print("Accommodation Name:", acc_type[user_choice - 1], file=bookingfile)
        print("Booking ID:", str(bookingid), file=bookingfile)
        print("Pool pass:", pool_pass, file=bookingfile)
        print("Number of people:", str(numbers_guests), file=bookingfile)
        print("Number of kids in kids club: ", str(kids_club), file=bookingfile)
        print("Cost", str(cost), file=bookingfile)

####################################### review booking ###############################################
def review_bookings(acc_type,numbers,extras_numbers):
    banner = 'LONG ISLAND HOLIDAYS – Review Bookings'
    print(banner)
    print('-' * len(banner))
    print(acc_type[0], numbers[0])
    print(acc_type[1], numbers[1])
    print(acc_type[2], numbers[2])
    
    print(f"Total No. Of Pool Passes : ",extras_numbers[1])
    print(f"No. Of Kids Club : ",extras_numbers[0])
    if numbers[0]>numbers[1] and numbers[0] > numbers[2]:
        print(f"Most Popular accomodation : ", acc_type[0])
    elif numbers[1]>numbers[0] and numbers[1] > numbers[2]:
        print(f"Most Popular accomodation : ", acc_type[1])
    elif numbers[2]>numbers[0] and numbers[2]>numbers[1]:
        print(f"Most Popular accomodation : ", acc_type[2])
    
    total1=numbers[0]*2000
    total2=numbers[1]*1600
    total3=numbers[2]*200
    kid=extras_numbers[0]*100
    pool=extras_numbers[1]*150
    
    expected_income=total1+total2+total3+kid+pool
    
    
    print(f'Expected Income : {expected_income}')
    average = expected_income / sum(numbers)
    print(f'Average Income : {average}')
    sites=30-sum(numbers)
    print(f'Remaining sites : {sites}')

##################################### main function #############################################
def main():
    acc_type, price, numbers = reading_bookings()
    extras, extras_numbers = reading_extras()

    banner = 'LONG ISLAND HOLIDAYS'
    print(banner)
    print('=' * len(banner))
    while True:
        try:
            choice = int(input(f"1. Make a Booking  \n2. Review Bookings \n3. Exit\n=>"))
            if choice == 3:
                break
            elif choice == 1:
                make_booking(acc_type, price, numbers, extras, extras_numbers)

            elif choice == 2:
                review_bookings(acc_type,numbers,extras_numbers)
            else:
                print(f'please enter a valid choice 1-3')
        except ValueError:
            print(choice)
            print(f'Please enter a number 1-3')

main()