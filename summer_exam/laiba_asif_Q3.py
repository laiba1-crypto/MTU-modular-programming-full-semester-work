#Name: LAIBA ASIF
#StudentID: R00201303

def read_lists(filename):
    lst_coffee = []
    lst_sales = []
    
    coffee = open(filename, "r")
    data = coffee.read()
    
    file = coffee_data.split("\n")
    for line in file:
            line = line.split(',')
            coffee.append(line[0])
            sales.append(line[1])
    return lst_coffee, lst_sales
def sort_by_cups(lst_coffee, lst_sales):
    sort = []
    for key, coffee in enumerate(lst_coffee):
        if int(lst_sales[key]) > 30:
            sort.append(coffee)
    return sort
        

def main():
    filename = input(f"Enter name of the file: ")
    lst_coffee, lst_sales = read_lists(filename)
    sort = sort_by_cups(lst_coffee, lst_sales)
    
main()