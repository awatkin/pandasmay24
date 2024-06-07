import pandas as pd


''' Tasks to be completed
The solution must also identify trends and patterns over a period of time for:

Completed in this code: The Total sales for each Revenue Streams
Completed in this code: The average sales for AM vs PM for a selected Revenue Stream
Completed in this code: The sales of a selected Revenue stream over a period of days selected by the user
Completed in this code: A comparison of AM sales Vs PM sales combining all revenue streams.'''


#  solution 1, 2, 3 and 4 below


def getdf():  # new subroutine to import a clean dataframe and return it.
    df = pd.read_csv("Task4_tester.csv")  # reads in the csv using pandas into a dataframe
    return df  # sends the dataframe back to the calling subroutine.


def ampmallstreams():  # New subroutine to solve task 4
    df = getdf()  # Gets in a clean dataframe
    df1 = df[['Time', 'Tickets', 'Gift Shop', 'Snack Stand', 'Pictures']]  # copies only the needed columns into df1
    df1 = df1.groupby('Time').sum()  # Sums the totals for AM and PM
    df2 = df[['Time', 'Tickets', 'Gift Shop', 'Snack Stand', 'Pictures']]  # Copies only the needed columns into df2
    df2 = df2.groupby('Time').sum().sum(axis=1)  # groups and sums, axis1 needed for AM and PM not by col
    return df1, df2  # Returns the two data series for printing


def revstreamdays():  # New subroutineto solve task 3
    df = getdf()  # gets in a clean dataframe
    revstream = get_revstream_choice()  # gets the yusers revenue stream choice
    numofdays = int(input("How many days do you want? "))  # takes the number of days they want to see in
    numofdays = numofdays * 2  # as eachday is 2 rows, multiplys the number
    df1 = df[['Day', 'Time', revstream]]  # Removes the columns of data not needed
    df1 = df1.iloc[:numofdays, :]  # Uses iloc to removce the rows now needed
    return df1  # returns the dataframe for output


def amvspmsales():  # new subroutine to solve task 2
    df = getdf()  # gets in a clean dataframe
    revstream = get_revstream_choice()  # gets the users revenue stream choice
    df1 = df[['Time', revstream]]  # takes just Time and the selected revstream forward
    df1 = df1.groupby('Time').mean()  # uses groupby and mean() to provide the average
    return df1  # returns the needed dataseries


def revstreamtotals():  # Added a new subroutine (at the top) to get totals
    df = getdf()  # This calls the new subroutine above to get a clean dataframe
    df1 = df[['Tickets', 'Gift Shop', 'Snack Stand', 'Pictures']]  # Copies only needed columns from df to the new df1
    df1 = df1.sum()  # This runs a sum function on each column and makes it into a series
    return df1  # This returns the calculated series


# Displays the main menu and collects choice of menu item


def menu():

    flag = True

    while flag:
        print("###############################################")
        print("Welcome! Please choose an option from the list")
        print("1. Show sales for a specific Revenue Stream")
        print("2. Show total sales for each revenue stream")  # Added a new menu option for solution 1
        print("3. Average sales for AM vs PM for a selected Revenue Stream")  # Added a new menu option for solution 2
        print("4. Sales for selected Revenue Stream for a number of days")  # Added a menu option for solution 3
        print("5. AM vs PM for a selected Revenue Stream")  # Added a menu option for solution 4

        main_menu_choice = input("Please enter the number of your choice (1-5): ")  # Adjusted text for more options

        try:
            int(main_menu_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("You generated the following error: ", e)
            flag = True
        else:
            if int(main_menu_choice) < 1 or int(main_menu_choice) > 5:  # changed 4 to 5 for option choices
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                return int(main_menu_choice)    

# Menu item selection form user and validates it


def get_revstream_choice():

    flag = True

    while flag:
        print("######################################################")
        print("Please choose a revenue stream form the list:")
        print("Please enter the number of the item (1-8)")
        print("1.  Tickets")
        print("2.  Gift Shop")
        print("3.  Snack Stand")
        print("4.  Pictures")
        print("######################################################")

        menu_list = ["Tickets", "Gift Shop", "Snack Stand", "Pictures"]

        item_choice = input("Please enter the number of your choice (1-4): ")

        try:
            int(item_choice)
        except Exception as e:
            print("Sorry, you did not enter a valid choice")
            print("The following error was generated: ", e)
            flag = True
        else:
            if int(item_choice) < 1 or int(item_choice) > 4:
                print("Sorry, you did not enter a valid choice")
                flag = True
            else:
                item_name = menu_list[int(item_choice)-1]
                return item_name


# imports data set and extracts data and returns data for a specific revenue stream
def get_selected_item(item):
  
    df1 = pd.read_csv("Task4_tester.csv") 
    df2 = df1[['Day', 'Time', item]]

    return df2

     
main_menu = menu()
if main_menu == 1:

    revStream = get_revstream_choice()
 
    extracted_data = get_selected_item(revStream)

    print("Here is the sales data for {} :".format(revStream))
    print(extracted_data)

elif main_menu == 2:  # New menu item checked for - solution 1
    totals = revstreamtotals()  # captures the returned dataframe / series to print
    print("Here is the total sales for each revenue stream:")  # Pre-cursor message for usability
    print(totals)  # Prints out the returned data series
elif main_menu == 3:  # New menu item checked for - solution 2
    totals = amvspmsales()  # captures the returned results
    print("Here is the average AM vs PM sales for a selected revenue stream:")  # message for readability
    print(totals)  # prints out the returned data
elif main_menu == 4:
    totals = revstreamdays()
    print("Here is the total sales for a selected revenue stream for your number of days:")  # Message for readability
    print(totals)  # Prints the totals out for the user
elif main_menu == 5:
    totalsind, totals = ampmallstreams()  # captures the returned results
    print("Here is the AM and PM sales for each of the Revenue Streams ")  # message for readability
    print(totalsind)  # Outputs the results
    print("Here is the total AM vs PM sales combining all Revenue Streams")
    print(totals)
else:
    print('This part of the program is still under development')
