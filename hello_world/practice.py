import json
import re

# File to store contacts
CONTACTS_FILE = "contacts.json"

# Load existing contacts
def load_contacts():
    """Load contacts from a file."""
    try:
        with open(CONTACTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save contacts to a file
def save_contacts():
    """Save contacts to a file."""
    with open(CONTACTS_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Validation functions
def validate_phone(phone_number):
    """Validate the phone number format."""
    return phone_number.isdigit() and 10 <= len(phone_number) <= 15

def validate_email(email):
    """Validate the email format."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Contact management functions
def add_contact(name, phone_number, email):
    """Add a new contact with validation."""
    if not validate_phone(phone_number):
        print("Invalid phone number. Please enter digits only (10-15 characters).")
        return
    if not validate_email(email):
        print("Invalid email address. Please enter a valid email.")
        return
    contacts[name] = {"phone_number": phone_number, "email": email}
    print(f"Contact for '{name}' added successfully!")
    save_contacts()

def all_contacts():
    """Display all contacts sorted by name."""
    if not contacts:
        print("No contacts available.")
    else:
        print("\nAll Contacts:")
        for name, details in sorted(contacts.items()):
            print(f"Name: {name}, Phone Number: {details['phone_number']}, Email: {details['email']}")

def search_contact(name):
    """Search for a contact by name."""
    if name in contacts:
        print(f"\nContact Found:\nName: {name}, Phone Number: {contacts[name]['phone_number']}, Email: {contacts[name]['email']}")
    else:
        print(f"No contact found for '{name}'.")

def update_contact(name, phone_number, email):
    """Update an existing contact."""
    if name in contacts:
        if not validate_phone(phone_number):
            print("Invalid phone number. Please enter digits only (10-15 characters).")
            return
        if not validate_email(email):
            print("Invalid email address. Please enter a valid email.")
            return
        contacts[name] = {"phone_number": phone_number, "email": email}
        print(f"Contact for '{name}' updated successfully.")
        save_contacts()
    else:
        print(f"No contact found for '{name}'. Please add it instead.")

def delete_contact(name):
    """Delete a contact by name."""
    if name in contacts:
        del contacts[name]
        print(f"Contact for '{name}' deleted successfully.")
        save_contacts()
    else:
        print(f"No contact found for '{name}'.")

# Main program
contacts = load_contacts()

while True:
    print("\n--- Contact Book ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search for a Contact")
    print("4. Update a Contact")
    print("5. Delete a Contact")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ").strip()
    
    if choice == "1":
        name = input("Enter name: ").strip()
        phone_number = input("Enter phone number: ").strip()
        email = input("Enter email: ").strip()
        add_contact(name, phone_number, email)
    elif choice == "2":
        all_contacts()
    elif choice == "3":
        name = input("Enter name to search: ").strip()
        search_contact(name)
    elif choice == "4":
        name = input("Enter name to update: ").strip()
        phone_number = input("Enter new phone number: ").strip()
        email = input("Enter new email: ").strip()
        update_contact(name, phone_number, email)
    elif choice == "5":
        name = input("Enter name to delete: ").strip()
        delete_contact(name)
    elif choice == "6":
        print("Exiting Contact Book. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")
