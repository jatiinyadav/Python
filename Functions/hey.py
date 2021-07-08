n = int(input("Enter no. of students: "))


class Section:

    def details(self):

        for i in student_list:
            print(i)


student_list = []

for i in range(1, n + 1):
    name = input("Enter name: ")
    roll = int(input("Enter roll no. of {}: ".format(name)))
    student_list.append(name)
    student_list.append(roll)

one = Section()

one.details()
