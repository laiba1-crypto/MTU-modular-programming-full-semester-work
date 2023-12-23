# 
def reading_bookings():
     file = open('Bookings_2022.txt', 'r')
     read = file.readlines()
     acc_type=[]
     price =[]
     numbers=[]
     for line in read:
          line_data = line.split(',')
          acc_type.append(line_data[0])
          price .append(float(line_data[1]))
          numbers.append(int(line_data[2]))

     return acc_type,price,numbers

def save_bookings(acc_type,price,numbers):

    with open('Bookings_2022.txt','w') as file_data:
        for i,item in enumerate(acc_type):
             print((item+','+str(price[i])+','+str(numbers[i])), file = file_data)

def reading_extras():
    file = open('extras.txt', 'r')
    read = file.readlines()
    extras=[]
    numbers=[]
    for line in read:
        line_dta = line.split(',')
        extras.append(line_dta[0])
        numbers.append(int(line_dta[1]))
    return extras,numbers
def save_extras(extras,numbers):

    with open('extras.txt', 'w') as file_data:
        for i,item in enumerate(extras):
            print((item+','+str(numbers[i])), file = file_data)
def main():

    acc_type,price,numbers = reading_bookings()
    #save_bookings(acc_type,price,numbers)
    extras, numbers = reading_extras()
    #save_extras(extras,numbers)



    banner = 'LONG ISLAND HOLIDAYS'
    print(banner)
    print('=' * len(banner))
    while  True:
        try:
            choice = int(input("1. Make a Booking  \n2. Review Bookings \n3. Exit\n=>"))
            if choice == 3:
                break
            elif choice == 1:
                print('make booking')
                # call the function to make bookings
                banner = "LONG ISLAND HOLIDAYS - MAKE A BOOKING"
                print(banner)
                print("=" * len(banner))
                while True:
                    try:
                        family = input("Enter Family name : ")
                        if 1 < len(family) <= 15:
                            break
                        else:
                            print('Family name must be between 1-15 characters')
                        continue
                    except ValueError:
                        print('Invalid input')
                        continue
                while True:
                    try:
                        phone = input("Enter Phone Number : ")
                        if 1 < len(phone) < 12:
                            break
                        else:
                            print('phone number must be less than 12 digits')
                            continue
                    except ValueError:
                        print('Invalid input')
                        continue
                count = 0
                count1 = 0
                count2 = 0
                choice = int(input(f"Choose Accomodation Type : \n1:Deluxe Caravan,(€2000),{count} booked\n2:Standard Caravan,(€1600),{count1} booked"
                                   f"\n3:Camp,(€200),{count2} booked \n4:No booking\n=>"))
                if choice == 1:
                    
            elif choice == 2:
                print('review bookings')
                # call the function to review the bookings
            else:
                print('please enter a valid choice 1-3')
        except ValueError:
            print('Please enter a number 1-3')


main()