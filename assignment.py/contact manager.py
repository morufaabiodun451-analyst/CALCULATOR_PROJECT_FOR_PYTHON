# Contact Manager using Dictionary

contacts = {}

while True:
    print("\n--- CONTACT MANAGER ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter your choice: ")

# Add Contact
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        contacts[name] = phone
        print(f"{name} added successfully!")

# View Contacts
    elif choice == "2":
        if contacts:
            print("\nContact List:")
            for name, phone in contacts.items():
                print(f"{name}: {phone}")
        else:
            print("No contacts found.")

# Search Contact
    elif choice == "3":
        search_name = input("Enter name to search: ")
        if search_name in contacts:
            print(f"{search_name}'s number is {contacts[search_name]}")
        else:
            print("Contact not found.")

# Delete Contact
    elif choice == "4":
        delete_name = input("Enter name to delete: ")
        if delete_name in contacts:
            del contacts[delete_name]
            print(f"{delete_name} deleted successfully!")
        else:
            print("Contact not found.")

# Exit
    elif choice == "5":
        print("Exiting Contact Manager...")
        break

    else:
        print("Invalid choice. Try again.")