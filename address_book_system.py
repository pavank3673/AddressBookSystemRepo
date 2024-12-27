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
    def __init__(self, contact_person):
        self.contact_person = contact_person

print("--- Enter contact details ---")
first_name = input("Enter first name : ")
last_name = input("Enter last name : ")
address = input("Enter address : ")
city = input("Enter city : ")
state = input("Enter state : ")
zip = input("Enter zip : ")
phone_number = input("Enter phone number : ")
email = input("Enter email : ")

contact_one = ContactPerson(first_name, last_name, address, city, state, zip, phone_number, email)
address_book_one = AddressBook(contact_one)

print(f"{address_book_one.contact_person} added to address book successfully")