# Function definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Main program
def calculator():
    print("Simple Calculator")
    
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    operation = input("Choose operation (+, -, *, /): ")
    
    if operation == "+":
        print("Result:", add(num1, num2))
    elif operation == "-":
        print("Result:", subtract(num1, num2))
    elif operation == "*":
        print("Result:", multiply(num1, num2))
    elif operation == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")

# Run the program
calculator()


contacts = {}

# Function to add contact
def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    contacts[name] = phone
    print("Contact added successfully!")

# Function to view contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

# Function to search contact
def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

# Function to delete contact
def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")

# Main menu function
def contact_manager():
    while True:
        print("\n1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

# Run program
contact_manager()