class Student:
    def __init__(self, name, id_no, marks):
        self.name = name
        self.id = id_no
        self.marks = marks

    def result(self):
        if self.marks >= 300:
            return "first_division"
        else:
            if self.marks < 300 and self.marks >= 250:
                return "second_division"
            else:
                if self.marks < 250 and self.marks >= 200:
                    return "third_division"
                else:
                    return "fail"


# user defined function is here, above are the user defined classes and methods
def options():
    while 1:
        print("0. Hit 0 to exit")
        print("1. View all student's detail list")
        print("2. View details of particular students")
        print("3. View 1st division list")
        print("4. View 2nd division list")
        print("5. View 3rd division list")
        print("6. View failed students list")
        print("7. View all student's detail list with result")
        print("Enter 1 or 2")
        print("\n")
        choice = int(input("Enter your choice"))  # taking user choice
        
        # if user choose to View all student's detail list
        if choice == 1:
            objects = []  # creating a list to add all the objects and display it in the form of list
            for obj in students_details:
                objects.append([obj.id, obj.name, obj.marks, obj.result()])

            print(objects)
            print("\n")  # just a line break
        #  if user choose to View details of particular students
        elif choice == 2:
            ask = input("Enter name of candidate:")  # asking for name of the student whose detail to be searched
            search_result = []  # creating a list to add all the objects with given name and display it in form of list
            for x in students_details:
                if x.name == ask:
                    search_result.append(x) # adding the desired result to a list
                else:
                    pass
            for i in search_result:
                print(i.name, i.id, i.marks, i.result())
            print("\n") # just a line break
        # if user choose to View detailed list of students with 1st division
        elif choice == 3:
            first_div = [] # creating a list to add 1st div student detail and display it in form of list
            for x in students_details:
                if x.result() == "first_division":
                    first_div.append(x) # adding desired objects to list
            for i in first_div:
                print(i.name, i.id, i.marks, i.result())
            print("\n") # just a line break
        elif choice == 4:
            second_div = [] # creating a list to add 2nd div student detail and display it in form of list
            for x in students_details:
                if x.result() == "second_division":
                    second_div.append(x) # adding desired objects to list
            for i in second_div:
                print(i.name, i.id, i.marks, i.result())
            print("\n") # just a line break
        elif choice == 5:
            third_div = [] # creating a list to add 3rd div student detail and display it in form of list
            for x in students_details:
                if x.result() == "third_division":
                    third_div.append(x) # adding desired objects to list
            for i in third_div:
                print(i.name, i.id, i.marks, i.result())
            print("\n") # just a line break
        elif choice == 6:
            fail = [] # creating a list to add failed student detail and display it in form of list
            for x in students_details:
                if x.result() == "fail":
                    fail.append(x) # adding desired objects to list
            for i in fail:
                print(i.name, i.id, i.marks, i.result())
            print("\n") # just a line break
        # if user choose to exist
        elif choice == 0:
            break

    #   if user choose to View all student's detail list with result
    #   here the output will be a dictionary with the result as key and a list as its value
    #   the list as value contains lists of object corresponding to the key result
    #   elif choice == 7:
    #     first_div = []
    #     second_div = []
    #     third_div = []
    #     fail = []
    #     detailed_result = {}
    #     for x in students_details:
    #         if x.result() == "first_division":
    #             first_div.append(x)
    #             detailed_result['1st_Division'] = first_div
    #         elif x.result() == "second_division":
    #             second_div.append(x)
    #             detailed_result['2nd_Division'] = second_div
    #         elif x.result() == "third_division":
    #             third_div.append(x)
    #             detailed_result['3rd_Division'] = third_div
    #         else:
    #             fail.append(x)
    #             detailed_result['FAIL'] = fail
    #     for key, value in detailed_result:
    #         print(key + ":")
    #         for ele in value:
    #             for x in ele:
    #                 print(x.name, x.marks, x.result)


# your program starts from below line, above all are user defined classes and functions
n = int(input("Enter number of students in class="))
print("\n")
print("Enter students details below:")

students_details = []
for i in range(n):
    name = input("Enter name of student=")
    id_no = int(input("Enter id of student="))
    marks = int(input("Enter marks of student="))
    students_details.append(Student(name, id_no, marks))
    print("Entry successful")

print("\n")
options()
