def read_data_from(filename):
    list_names = []
    list_attendance = []

    with open(filename) as data:
        for line in data:
            line_data = line.split(',')
            list_names.append(line_data[0])
            list_attendance.append(int(line_data[1]))
    return list_names, list_attendance

def less_than_50(n,a):
    low_attendance = []
    for i, name in enumerate(n):
        if a[i] <5:
            low_attendance.append(n)
    return low_attendance
def main():
    names, attend = read_data_from('data.txt.py')
    print(less_than_50(n,a))
main()
