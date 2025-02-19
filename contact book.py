# Dictionary to store contacts

print("welcome to the Contact book program !!")
print("--------------------------------------")
contacts = {}  
def add_contact():
    # Adds a new contact to the contact book.
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts[name] = {"phone": phone, "email": email, "address": address}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    # Displays all contacts with their phone numbers.
    if not contacts:
        print("Contact book is empty.")
    else:
        print("Contacts:")
        for name, details in contacts.items():
            print(f"- {name}: {details['phone']}")

def search_contact():
    # Searches for a contact by name or phone number.
    search_term = input("Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term == details["phone"]:
            print(f"Contact found: {name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
            print(f"Address: {details['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    # Updates the details of an existing contact.
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("Current details:")
        print(f"Phone: {contacts[name]['phone']}")
        print(f"Email: {contacts[name]['email']}")
        print(f"Address: {contacts[name]['address']}")

        update_field = input("Enter the field to update (phone, email, address, or all): ").lower()
        if update_field == "phone":
            contacts[name]["phone"] = input("Enter new phone number: ")
        elif update_field == "email":
            contacts[name]["email"] = input("Enter new email address: ")
        elif update_field == "address":
            contacts[name]["address"] = input("Enter new address: ")
        elif update_field == "all":
            contacts[name]["phone"] = input("Enter new phone number: ")
            contacts[name]["email"] = input("Enter new email address: ")
            contacts[name]["address"] = input("Enter new address: ")
        else:
            print("Invalid field.")
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    """Deletes a contact from the contact book."""
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
print("Program successfully executed ;))")