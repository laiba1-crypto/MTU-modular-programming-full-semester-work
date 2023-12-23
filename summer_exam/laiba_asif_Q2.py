#Name: LAIBA ASIF
#StudentID: R00201303

def add_to_lst():
    lst_month =['january', 'february', 'march', 'april', 'may']
    car_sales =['45', '101', '65', '52', '32']
    ques = int(input(f"Enter sales figures for june: "))
    lst_month.append("June")
    car_sales.append(ques)
    return lst_month, car_sales

def profit(lst_month, car_sales):
    print("___________________")
    combine = []
    for i in range(car_sales):
        mon = intput(f"enter car sales {i*1500}")
        combine.append(mon)
    for i in range(lst_month) :
        if mon<= 90000:
            print({lst_month*1500} )
    return car_sales, lst_month
    #combine = zip(lst_month, car_sales)
    #for Month, Qty in combine:
        #print(Month,Qty*1500)
def main():
    lst_month, car_sales  = add_to_lst()
    profit(lst_month, car_sales)
    
    