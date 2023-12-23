def get_positive_int(prompt):
    num = input(prompt)
    return num
def get_string(prompt):
    answer = input(prompt)
    return answer


def main():
    num = get_positive_int('what are your marks')
    print(num)
    comment = get_string('what is the comment')
    print(comment)

main()