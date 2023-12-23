from classesrevision import Patient
def ward(patient):
    if patient.age< 16:
        print('paeds ward')
    else:
        print('general ward')
def main():
    patient1 = Patient(1,22,'f') #no '' around numbers
    print(patient1)
    ward(patient1)
main()