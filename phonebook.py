def display_menu():
    print("\nPhoneBook menu:")
    print("1: ADD CONTACT:")
    print("2: DELETE CONTACT:")
    print("3: UPDATE CONTACT:")
    print("4: SEARCH CONTACT:")
    print("5: DISPLAY ALL CONTACTS:")
    print("6:EXIT")

def ADD_CONTACT(phonebook):
    name= input("Enter name: ").strip()
    if name in phonebook:
        print(f"Contact {name} already exists")
    else:
        phone=input("Enter the phone number: ").strip()
        phonebook[name]=phone
        print(f"Contact {name} added successfully")

def DELETE_CONTACT(phonebook):
    name = input("Enter name: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully")
    else:
        print(f"Contact {name} not found")

def UPDATE_CONTACT(phonebook):
    name = input("Enter name: ").strip()
    if name in phonebook:
        phone=input("Enter the number:").strip()
        phonebook[name]=phone
    else:
        print(f"Contact {name} not found")

def SEARCH_CONTACT(phonebook):
    name = input("Enter name: ").strip()
    if name in phonebook:
        print(f"Contact {name} : {phonebook[name]}")
    else:
        print(f"Contact {name} not found")

def DISPLAY_ALL_CONTACTS(phonebook):
    if phonebook:
        print("\nContacts:")
        for name in sorted(phonebook):
            print(f"{name} : {phonebook[name]}")
    else:
        print("No Contacts Found")

def main():
    phonebook={}
    while True:
        display_menu()
        choice=int(input("Enter your choice from 1-6: "))

        if choice == 1:
            ADD_CONTACT(phonebook)
        elif choice == 2:
            DELETE_CONTACT(phonebook)
        elif choice == 3:
            UPDATE_CONTACT(phonebook)
        elif choice == 4:
            SEARCH_CONTACT(phonebook)
        elif choice == 5:
            DISPLAY_ALL_CONTACTS(phonebook)
        elif choice== 6:
            print("Exiting phonebook")
        else:
            print("Invalid choice.Please try again")


if __name__=="__main__":
    main()

