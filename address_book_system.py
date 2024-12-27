print("Welcome to Address Book Program")

class ContactPerson:
    def __init__(self, first_name, last_name, address, city, state, zip, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip = zip
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Contact of {self.first_name} {self.last_name} with phone number : {self.phone_number}"
    
class AddressBook:
    def __init__(self):
        self.contact_person = None

    def add_contact(self):
        print("--- Enter contact details ---")
        first_name = input("Enter first name : ")
        last_name = input("Enter last name : ")
        address = input("Enter address : ")
        city = input("Enter city : ")
        state = input("Enter state : ")
        zip = input("Enter zip : ")
        phone_number = input("Enter phone number : ")
        email = input("Enter email : ")

        new_contact = ContactPerson(first_name, last_name, address, city, state, zip, phone_number, email)
        self.contact_person = new_contact

    def edit_contact(self):
        first_name = input("Enter contact person name to edit : ")
        if self.contact_person.first_name != first_name:
            print(f"Contact person {first_name} does not exists in address book")
        else:
            print("--- Enter contact details ---")
            self.contact_person.address = input("Enter address : ")
            self.contact_person.city = input("Enter city : ")
            self.contact_person.state = input("Enter state : ")
            self.contact_person.zip = input("Enter zip : ")
            self.contact_person.phone_number = input("Enter phone number : ")
            self.contact_person.email = input("Enter email : ")

address_book_one = AddressBook()
address_book_one.add_contact()
print(f"{address_book_one.contact_person} added to address book successfully")

address_book_one.edit_contact()
print(f"{address_book_one.contact_person} edited in address book successfully")