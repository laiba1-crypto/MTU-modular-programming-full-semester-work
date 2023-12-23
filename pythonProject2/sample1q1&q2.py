#sample1 BMI calculator

def user_details():
    weight = float(input('enter your weight in kg(s):'))
    height = float(input('enter your height in meters:'))
    return weight, height

def cal_bmi(weight,height):
    bmi = weight/(height**2)
    return bmi

def get_sentence():
    sentence = str(input('enter the text:'))
    return sentence.replace('','_')

list_days = ['mon','tue','wed','thur','fri']
list_hours = [2.5, 4, 4, 2, 5]
for i, day in enumerate(list_days):
    print(day,list_hours[i])

list_days.append('sat')
list_days.append('sun')

for i in range(2):
    hour = float(input(f'how many hours your worked on {list_days[i-2]}'))#-2 to get last 2 objects
    list_hours.append(hour)

rate = 12
for i, day in enumerate(list_days):
    print(f'{day} {rate * list_hours[i]}')


def main():
    w, h = user_details()
    bmi = cal_bmi(w, h)
    s = get_sentence()
    print(s)
    print(f'your BMI is: {bmi:.2f}') #.2f i.e format the answer to 2 decimal places
main()