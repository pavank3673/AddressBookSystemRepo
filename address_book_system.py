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
    
    def __eq__(self, value):
        if isinstance(value, self.__class__):
            return self.first_name == value.first_name
        else:
            return False

class AddressBook:
    address_books = dict()
    city_dictionary = dict()
    state_dictionary = dict()

    def __init__(self):
        self.contact_persons = []

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
        
        flag = False
        for ele in self.contact_persons:
            if ele == new_contact:
                flag = True
                break

        if flag == True:
            print(f"Contact person {new_contact.first_name} alredy exists")
        else:
            self.contact_persons.append(new_contact)

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

    def delete_contact(self):
        first_name = input("Enter contact person name to delete : ")
        if self.contact_person.first_name != first_name:
            print(f"Contact person {first_name} does not exists in address book")
        else:
            del self.contact_person
    
    @classmethod
    def add_address_book(cls):
        address_book_name = input("Enter new address book name : ")
        if address_book_name in cls.address_books:
            print(f"Address book with name {address_book_name} already exists")
        else:
            cls.address_books[address_book_name] = AddressBook()

    @classmethod
    def search_contact(cls):
        search_criteria = input("Enter search contact criteria, city or state : ")
        if search_criteria == "city":
            city_name = input("Enter city name : ")
            for address_book in cls.address_books:
                for contact_person in cls.address_books[address_book].contact_persons:
                    if contact_person.city == city_name:
                        print(contact_person)
        elif search_criteria == "state":
            state_name = input("Enter state name : ")
            for address_book in cls.address_books:
                for contact_person in cls.address_books[address_book].contact_persons:
                    if contact_person.state == state_name:
                        print(contact_person)

    @classmethod
    def view_contact(cls):
        cls.city_dictionary.clear()
        cls.state_dictionary.clear()

        view_criteria = input("Enter view criteria, city or state : ")
        if view_criteria == "city":
            for address_book in cls.address_books:
                for contact_person in cls.address_books[address_book].contact_persons:
                    if contact_person.city in cls.city_dictionary:
                        cls.city_dictionary[contact_person.city].append(contact_person)
                    else:
                        cls.city_dictionary[contact_person.city] = []
                        cls.city_dictionary[contact_person.city].append(contact_person)
            
            for city ,contacts in cls.city_dictionary.items():
                print(f"City: {city}")
                for contact in contacts:
                    print(contact)

        elif view_criteria == "state":
            for address_book in cls.address_books:
                for contact_person in cls.address_books[address_book].contact_persons:
                    if contact_person.state in cls.state_dictionary:
                        cls.state_dictionary[contact_person.state].append(contact_person)
                    else:
                        cls.state_dictionary[contact_person.state] = []
                        cls.state_dictionary[contact_person.state].append(contact_person)

            for state, contacts in cls.state_dictionary.items():
                print(f"State : {state}")
                for contact in contacts:
                    print(contact)

    @classmethod
    def count_contact(cls):
        count_criteria = input("Enter count contact criteria, city or state : ")
        if count_criteria == "city":
            city_count = dict()
            for address_book in cls.address_books:
                for contact_person in cls.address_books[address_book].contact_persons:
                    if contact_person.city in city_count:
                        city_count[contact_person.city] += 1
                    else:
                        city_count[contact_person.city] = 0
                        city_count[contact_person.city] += 1
                    
            for city, count in city_count.items():
                print(f"City : {city}, Count : {count}")

        elif count_criteria == "state":
            state_count = dict()
            for address_book in cls.address_books:
                for contact_person in cls.address_books[address_book].contact_persons:
                    if contact_person.state in state_count:
                        state_count[contact_person.state] += 1
                    else:
                        state_count[contact_person.state] = 0
                        state_count[contact_person.state] += 1

            for state, count in state_count.items():
                print(f"State : {state}, Count : {count}")

    @staticmethod
    def sort_func(value):
        return value.first_name  

    @classmethod
    def sort_contact(cls):
        sort_criteria = int(input("Choose sort criteria \n1. Ascending \n2. Descending \n"))
        if sort_criteria == 1:
            for address_book in cls.address_books:
                print(f"Address book : {address_book}")
                cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_func)
                for contact_person in cls.address_books[address_book].contact_persons:
                    print(contact_person)
                
        elif sort_criteria == 2:
            for address_book in cls.address_books:
                print(f"Address book : {address_book}")
                cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_func, reverse = True)
                for contact_person in cls.address_books[address_book].contact_persons:
                    print(contact_person)

    @staticmethod
    def sort_city_func(value):
        return value.city

    @staticmethod
    def sort_state_func(value):
        return value.state

    @staticmethod
    def sort_zip_func(value):
        return value.zip

    @classmethod
    def sort_entries(cls):
        sort_criteria = int(input("Choose sort criteria \n1. City \n2. State \n3. Zip \n"))
        sort_order = int(input("Choose sort order \n1. Ascending \n2. Descending \n"))
        if sort_criteria == 1:
            for address_book in cls.address_books:
                if sort_order == 1:
                    cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_city_func)
                elif sort_order == 2:
                     cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_city_func, reverse = True)
                print(f"Address book : {address_book}")
                for contact_person in cls.address_books[address_book].contact_persons:
                    print(contact_person)
            
        elif sort_criteria == 2:
            for address_book in cls.address_books:
                if sort_order == 1:
                    cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_state_func)
                elif sort_order == 2:
                     cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_state_func, reverse = True)
                print(f"Address book : {address_book}")
                for contact_person in cls.address_books[address_book].contact_persons:
                    print(contact_person)

        elif sort_criteria == 3:
            for address_book in cls.address_books:
                if sort_order == 1:
                    cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_zip_func)
                elif sort_order == 2:
                     cls.address_books[address_book].contact_persons.sort(key= AddressBook.sort_zip_func, reverse = True)
                print(f"Address book : {address_book}")
                for contact_person in cls.address_books[address_book].contact_persons:
                    print(contact_person)


AddressBook.add_address_book()
address_book_name = input("Enter existing address book name : ")
AddressBook.address_books[address_book_name].add_contact()
AddressBook.address_books[address_book_name].add_contact()

AddressBook.add_address_book()
address_book_name = input("Enter existing address book name : ")
AddressBook.address_books[address_book_name].add_contact()
AddressBook.address_books[address_book_name].add_contact()

AddressBook.sort_entries()