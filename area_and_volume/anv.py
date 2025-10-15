
def rect_area():
    chkflg = True
    while chkflg:
        print("########### Area of a Rectangle #############")
        print("####### Please enter the needed info ########")
        length = input("Enter Length: ")
        width = input("Enter Width: ")
        try:
            length = float(length)
            width = float(width)
            area = length * width
            chkflg = False
            return area
        except:
            print("Please enter a valid number for each option")

def main_menu():
    chkflg = True
    while chkflg:
        print("########### Please select an option #############")
        print("### 1. ")
        print("### 1. ")
        print("### 1. ")
        print("### 9. Quit")
        choice = input("Enter a menu choice: ")
        try:
            choice = int(choice)
            chkflg = False
            return choice
        except ValueError:
            print("Please enter a valid choice.")


def main():
    chkflg = True
    while chkflg:
        choice = main_menu()

        if choice == 9:
            quit()
        else:
            print("Please enter a valid choice.")



if __name__ == '__main__':
    main()