"""###################################################################################################
# This is a simple Contact List Script in which you can store contacts with number and can update or delete contact
####################################################################################################"""

# This a dictionary in contains number and names
contacts = {"adil": "03111311993", "ali": "03452156199", "ahmed": "035464494949", "faraz": "03584944949"}

# Main function


def main():

    # Main Menu
    print ("\n******Main Menu******")
    print("Enter (1) For All Contacts")
    print("Enter (2) To ADD New Contact")
    print("Enter (3) To Change Existing Contact")
    print("Enter (4) To Delete a Contact")
    print("Enter (5) To Delete all Contacts")

# Getting user choice and storing it in ( menu_selection) variable
    try:
        menu_selection = 0
        menu_selection = int(raw_input("Select : "))
    except ValueError:
        print("\nPlz Select 1 to 5 Value from the Menu !!! \n")
        main()

######################################################
    # """ Menu Selection Conditions  """
######################################################

    # Display All contacts in the Dictionary
    if menu_selection == 1:
        print("\n*****Contact List ***")
        for key, values in contacts.items():
            print(key + " : " + values)
        main()

    # Adding New contact in the Dictionary
    elif menu_selection == 2:
        new_contact_name = raw_input("Enter Name : ")

        # Getting Name From user
        new_contact_name = new_contact_name or "abc"

        # Getting Number from User
        try:
            new_contact_number = int(raw_input("Enter Number : "))
        except ValueError:
            print ("\nPlz Select Correct Number")
            main()
        new_contact_number = new_contact_number or 0
        if new_contact_name == "abc":
            print ("\nPlz Select Correct Name ! ")
            main()
        if new_contact_number == 0:
            print ("\nPlz Select Correct Number ! ")
            main()
        else:
            print("\nContact Added successfully !!! ")
            contacts[new_contact_name] = str(new_contact_number)
            main()

    # Updating existing contact here
    elif menu_selection == 3:
        contact_update_name = raw_input("Enter Name : ")
        if contact_update_name in contacts.keys():
            try:
                update_contact_number = int(raw_input("Enter Number : "))
                contacts[contact_update_name] = str(update_contact_number)
                print("\nNumber Updated successfully !!! ")
                main()
            except ValueError:
                print ("\nPlz Select Correct number !!!")
                main()
        else:
            print("\nName Not Exist !!!")
            main()

    # Deleting existing contact from the dictionary
    elif menu_selection == 4:
        del_contact_name = raw_input("Enter Name : ")
        if del_contact_name in contacts.keys():
            check = raw_input("\nWarning !! The contact will be permanently delete if Yes press (y) ")
            if check == "y" or check == "Y":
                del contacts[del_contact_name]
                print("\nContact Deleted\n")
            else:
                print("\nContact not deleted\n")
                main()
        else:
            print("Name Not Exist !!!")
            main()

# Deleting all contacts from existing contact from the dictionary
    elif menu_selection == 5:
        check = raw_input("\nWarning !! All contacts will be permanently delete\n if Yes press (y) ")
        if check == "y" or check == "Y":
            contacts.clear()
            print("\n All Contacts permanently Deleted !! ")
            main()
        else:
            print("\nContact not Deleted !!\n")
            main()

# If no option Selected
    else:
        print("\nPlz Select 1 to 5 Value from the Menu !!! \n")
        main()


# The program execution Start from here
if __name__ == '__main__':
    main()
main()
