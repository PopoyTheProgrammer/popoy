class Menu():

    student_list = []
 
    while True:
        option = input("Testing Choices" + "\n" + "*************************" + "\n" +
                   "1 - Create" + "\n" +
                     "2 - Read" + "\n" +
                     "3 - Update" + "\n" +
                   "4 - Delete" + "\n" +
                     "5 - Exit" + "\n" +
                    "What do you want? ")
    
        if option == '1':
            name = input("Add Student: ")
            student_list.append(name) 
        elif option == '2':
            print(student_list) 
        elif option == '3':
            index2 = int(input("Enter Student Index: ")) 
            name2 = str(input("Update Student: "))
            student_list[index2] = name2
        elif option == '4':
            name3 = input("Delete Student: ")
            student_list.remove(name3)
        elif option == '5':
            exit()
        else:
            print("Not valid!")
