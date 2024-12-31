class Contact:
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