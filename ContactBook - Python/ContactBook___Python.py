from prettytable import PrettyTable

class Contact(object):
    def __init__(self, name, surname, number):
        self.name = name
        self.surname = surname
        self.number = number


def create_contact():
    """Create a new contact and add it to the address book"""


    firstname = input("Firstname:\n")
    lastname = input("Lastname:\n")
    number = input("Phone:\n")
    contacts.append(Contact(firstname, lastname, number))


def delete_contact():
    """Delete a contact

    Ask user for the index of the customer wished to be deleted.
    The contact list is first shown so that index is easiest to find
    for the user. A single 'y' or 'Y' character is received as confirmation
    before deleting the class object.
    """
    if not contacts:
        print("Contact list is empty\n")
    else:
        show_contacts()
        try:
            delete_index = int(input("Enter contact position you'd like to delete: "))
            if (delete_index > len(contacts)):
                print("Please enter a index within range\n")
                delete_contact()
        except:
            print("Please be sure to enter an integer value\n")
            delete_contact()
        confirmation = input("Contact to delete: {} {}\nConfirm Y (Any other key to abort): ".format((contacts[delete_index - 1].name),(contacts[delete_index - 1].surname)))
        if (confirmation == 'y') or (confirmation == 'Y'):
            print("Contact deleted\n")
            del contacts[delete_index - 1]
        else:
            print("Delete contact aborted")


def show_contacts():
    """Display the address book

    Use prettytable for a easier readable table to display
    the contents of the contact list.
    """

    t = PrettyTable(['Pos', 'Name', 'Surname', 'Number'])
    for contact in contacts:
        t.add_row([contacts.index(contact) + 1, contact.name,
                   contact.surname, contact.number])
    print(t)


def init_contacts():
    """Adds dummy values at start of program"""

    contacts.append(Contact("Corey", "Motion", "0216249997"))
    contacts.append(Contact("Eisha", "Snell", "0275014906"))
    contacts.append(Contact("Harrison", "Blackford", "0203785143"))
    contacts.append(Contact("Jodan", "Scott-French", "0260733121"))


def main():
    """Main function of the program

    Runs continuously and calls other functions 
    as per user commands.
    """

    global contacts
    contacts = []
    init_contacts()
    while True:
        print("==== Address book command page =====")
        command = input("a - add new contact\nd - delete contact\ns - show contacts\nq - quit\n")
        if command == 'a':
            create_contact()
        elif command == 'd':
            delete_contact()
        elif command == 's':
            show_contacts()
        elif command == 'q':
            break


main()

