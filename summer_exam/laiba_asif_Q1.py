#Name: LAIBA_ASIF
#StudentID: R00201303

def f1():
    year = int(input(f'Enter year of birth:  '))
    month = input(f'Enter month of birth: ')
    return year, month

def f2(year, month):
    string = month
    year1 = str(year)
    string1 = year1
    print("Generated Password  : "+year1[0]+","+string[0].upper()+","+string[1].upper()+","+year1[3]+","+month.lower())


def main():
    year, month = f1()
    f2(year, month)

if __name__ == '__main__':
    main()