#Your task is to develop a Contact Management System with the following features:
#User Interface (UI):
#Create a user-friendly command-line interface (CLI) for the Contact Management System.
#Display a welcoming message and provide a menu with the following options:
#Welcome to the Contact Management System! 
#Menu:
#1. Add a new contact
#2. Edit an existing contact
#3. Delete a contact
#4. Search for a contact
#5. Display all contacts
#6. Export contacts to a text file
#7. Import contacts from a text file *BONUS*
#8. Quit

#Contact Data Storage:
#Use nested dictionaries as the main data structure for storing contact information.
#Each contact should have a unique identifier (e.g., a phone number or email address) as the outer dictionary key.
#Store contact details within the inner dictionary, including:
#Name
#Phone number
#Email address
#Additional information (e.g., address, notes).

#Menu Actions:
#Implement the following actions in response to menu selections:
#Adding a new contact with all relevant details.
#Editing an existing contact's information (name, phone number, email, etc.).
#Deleting a contact by searching for their unique identifier.
#Searching for a contact by their unique identifier and displaying their details.
#Displaying a list of all contacts with their unique identifiers.
#Exporting contacts to a text file in a structured format.
#Importing contacts from a text file and adding them to the system. * BONUS

#User Interaction:
#Utilize input() to enable users to select menu options and provide contact details.
#Implement input validation using regular expressions (regex) to ensure correct formatting of contact information.

#Error Handling:
#Apply error handling using try, except, else, and finally blocks to manage unexpected issues that may arise during execution.

#Optional Bonus Points
#Contact Categories (Bonus): Implement the ability to categorize contacts into groups (e.g., friends, family, work). Each contact can 
# belong to one or more categories.
#Contact Search (Bonus): Enhance the contact search functionality to allow users to search for contacts by name, phone number, email 
# address, or additional information.
#Contact Sorting (Bonus): Implement sorting options to display contacts alphabetically by name or based on other criteria.
#Backup and Restore (Bonus): Add features to create automatic backups of contact data and the ability to restore data from a backup 
# file.
#Custom Contact Fields (Bonus): Allow users to define custom fields for contacts (e.g., birthdays, anniversaries) and store this 
# information.


def display_menu():
    print("Welcome to the Contact Management System!")
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

def add_contact(contacts):
    print("Adding a new contact:")
    unique_id = input("Enter a unique identifier (e.g., phone number or email address): ")
    name = input("Enter the name: ")
    phone_number = input("Enter the phone number: ")
    email = input("Enter the email address: ")
    address = input("Enter the address: ")
    notes = input("Enter any additional notes: ")
    
    contacts[unique_id] = {
        'Name': name,
        'Phone Number': phone_number,
        'Email': email,
        'Address': address,
        'Notes': notes
    }
    print("Contact added successfully!")

def edit_contact(contacts):
    print("Editing an existing contact:")
    unique_id = input("Enter the unique identifier of the contact you want to edit: ")
    if unique_id in contacts:
        print("Current contact details:")
        print("Name:", contacts[unique_id]['Name'])
        print("Phone Number:", contacts[unique_id]['Phone Number'])
        print("Email:", contacts[unique_id]['Email'])
        print("Address:", contacts[unique_id]['Address'])
        print("Notes:", contacts[unique_id]['Notes'])
        
        choice = input("What would you like to edit? (1. Name, 2. Phone Number, 3. Email, 4. Address, 5. Notes): ")
        if choice == '1':
            contacts[unique_id]['Name'] = input("Enter the new name: ")
        elif choice == '2':
            contacts[unique_id]['Phone Number'] = input("Enter the new phone number: ")
        elif choice == '3':
            contacts[unique_id]['Email'] = input("Enter the new email address: ")
        elif choice == '4':
            contacts[unique_id]['Address'] = input("Enter the new address: ")
        elif choice == '5':
            contacts[unique_id]['Notes'] = input("Enter the new notes: ")
        else:
            print("Invalid choice.")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    print("Deleting a contact:")
    unique_id = input("Enter the unique identifier of the contact you want to delete: ")
    if unique_id in contacts:
        del contacts[unique_id]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact(contacts):
    search_key = input("Enter the unique identifier of the contact to search for: ")
    if search_key in contacts:
        print("Contact found:")
        contact_details = contacts[search_key]
        print("Name:", contact_details['Name'])
        print("Phone Number:", contact_details['Phone Number'])
        print("Email:", contact_details['Email'])
        print("Address:", contact_details['Address'])
        print("Notes:", contact_details['Notes'])
    else:
        print("Contact not found.")


def display_contacts(contacts):
    if contacts:
        print("All contacts:")
        for unique_id, contact_details in contacts.items():
            print("Unique Identifier:", unique_id)
            print("Name:", contact_details['Name'])
            print("Phone Number:", contact_details['Phone Number'])
            print("Email:", contact_details['Email'])
            print("Address:", contact_details['Address'])
            print("Notes:", contact_details['Notes'])
            print("-" * 30)
    else:
        print("No contacts available.")

def export_contacts(contacts):
    filename = "contacts.txt"
    with open(filename, "w") as file:
        for unique_id, contact_details in contacts.items():
            file.write(f"Unique Identifier: {unique_id}\n")
            file.write(f"Name: {contact_details['Name']}\n")
            file.write(f"Phone Number: {contact_details['Phone Number']}\n")
            file.write(f"Email: {contact_details['Email']}\n")
            file.write(f"Address: {contact_details['Address']}\n")
            file.write(f"Notes: {contact_details['Notes']}\n")
            file.write("-" * 30 + "\n")
    print(f"Contacts exported to '{filename}' successfully.")


def import_contacts(contacts):
    filename = "contacts.txt"
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            current_contact = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Unique Identifier:"):
                    unique_id = line.split(":")[1].strip()
                    current_contact = {'Name': '', 'Phone Number': '', 'Email': '', 'Address': '', 'Notes': ''}
                    contacts[unique_id] = current_contact
                elif line.startswith("Name:"):
                    current_contact['Name'] = line.split(":")[1].strip()
                elif line.startswith("Phone Number:"):
                    current_contact['Phone Number'] = line.split(":")[1].strip()
                elif line.startswith("Email:"):
                    current_contact['Email'] = line.split(":")[1].strip()
                elif line.startswith("Address:"):
                    current_contact['Address'] = line.split(":")[1].strip()
                elif line.startswith("Notes:"):
                    current_contact['Notes'] = line.split(":")[1].strip()
        print(f"Contacts imported from '{filename}' successfully.")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")

def main():
    contacts = {}
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ")
        
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            edit_contact(contacts)
        elif choice == '3':
            delete_contact(contacts)
        elif choice == '4':
            search_contact(contacts)
        elif choice == '5':
            display_contacts(contacts)
        elif choice == '6':
            export_contacts(contacts)
        elif choice == '7':
            import_contacts(contacts)
        elif choice == '8':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")

main()

