# Improved Contact Manager

contacts = {}

def add_contact():
    print("\n--- Add New Contact ---")
    name = input("Enter name: ").strip().title()

    if name in contacts:
        print("⚠️ Contact already exists!")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print(f"✅ {name} added successfully!")


def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("📭 No contacts available.")
        return

    for i, (name, info) in enumerate(contacts.items(), start=1):
        print(f"{i}. {name}")
        print(f"   📞 Phone: {info['phone']}")
        print(f"   📧 Email: {info['email']}")
        print("-" * 25)


def search_contact():
    print("\n--- Search Contact ---")
    search_name = input("Enter name: ").strip().title()

    if search_name in contacts:
        info = contacts[search_name]
        print(f"\n🔍 Contact Found:")
        print(f"Name: {search_name}")
        print(f"Phone: {info['phone']}")
        print(f"Email: {info['email']}")
    else:
        print("❌ Contact not found.")


def delete_contact():
    print("\n--- Delete Contact ---")
    name = input("Enter name: ").strip().title()

    if name in contacts:
        del contacts[name]
        print(f"🗑️ {name} deleted successfully!")
    else:
        print("❌ Contact not found.")


def menu():
    while True:
        print("\n" + "="*35)
        print("📱 CONTACT MANAGER SYSTEM")
        print("="*35)
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("👉 Enter your choice (1-5): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


# Run the program
menu()