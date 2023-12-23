from my_classes import Dog
def average_age(dogs):

    #no_of_dogs = len(dogs)
    #sum_of_ages = 0

    #for dog in dogs:
        #sum_of_ages += dog.age

    #return sum_of_ages/no_of_dogs
    return sun( [dog.age for dog in dogs])/len(dogs)
def print_list_to_file(dogs,filename):
    with open(filename,'w') as output:
        for dog in dogs:
            print(dog,file = output)
def main():
    dogs = [
        Dog('Freddie','1','King Charles'),
        Dog('Mickey', '6','Greyhound'),
        Dog('Ruby', '2', 'Mongrel'),
        Dog('Esme', '6', 'Lurcher')
            ]
        average = average_age(dogs)
        print(f'the average of dog is {average} years')

        print_list_to_file(dogs, 'dogs_output_txt')
    #for dog in dogs:
        #print(dog)
main()