# Author: laiba asif
# Purpose: assessment 2

#declared all the counties
counties = ('Cork','Kerry','Limerick','Wicklow','Carlow','Dublin','Donegal','Mayo','KilKenny','Waterford','Meath','Tipperary','Clare')

#declared all the months
months_year = ('january', 'february','march', 'april', 'may', 'june', 'july','august', 'september' ,'october', 'november' , 'december')

#Summer months
summer_months = ('june' , 'july', 'august')

#declared rainfall_result to concatenate
rainfall_result=""

Based_from = input('where are you based')

if Based_from.isalpha(): #only contains letters
    if Based_from in counties:

        month = input('enter month')
        if month in months_year:
        # month is valid
        #month in months year
            rainfall = int(input(f'what was the rainfall in {month}'))

            print(f'in {month} {rainfall}mm rain fell in the {Based_from} region')
            if month in summer_months:
                # summer month
                if rainfall >50:
                    print('this is high rainfall for summer months')
                elif rainfall <10:
                    print('this is low rainfall for summer months')
                else:
                    print('this is normal range for summer months')
            else : # non summer month
                if rainfall >100:
                    print('this is high rainfall for non summer month')
                    rainfall_result = "abnormally high"
                elif rainfall < 50:
                    print("This is low rainfall for non summer month")
                    rainfall_result="abnormally low"
                else:
                    rainfall_result = "in the normal range"
                #output for non summer month
                print(f"This is {rainfall_result} for non summer months")
        else:#not a valid month check
            print ("This is not a valid month")
    else: #not a valid county check
        print("This not a valid county")
#error validation for alphabets check only
else:
    print("This should only contains letter of alphabets.")