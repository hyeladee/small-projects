class AddressBook:
    def __init__(self) -> None:
        self.contacts = {}

    def normalize_name(self, name):
            return name.lower()
    
    def validate_phone(self, phone):
            if type(phone) == int:
                if phone > 0:
                    return True
            return False

    def add(self, name: str, phone: int, address: str) -> None:
        name = self.normalize_name(name)
        if self.validate_phone(phone):
            self.contacts[name] = f'{name}, {phone}, {address}'
        else:
            print(f'Phone number is not valid.')

    def edit(self, name: str, phone: int, address: str) -> None:
        name = self.normalize_name(name)
        if self.validate_phone(phone):
            try:
                self.contacts[name]
                self.contacts[name] = f'{name}, {phone}, {address}'
            except KeyError:
                print(f'Contact {name.title()} does not exist.')
        else:
            print(f'Phone number is not valid.')

    def delete(self, name: str) -> None:
        name = self.normalize_name(name)
        try:
            del self.contacts[name]
        except KeyError:
            print(f'Contact {name.title()} does not exist.')

    def view(self, name: str) -> None:
        name = self.normalize_name(name)
        try:
            print(self.contacts[name].title())
        except KeyError:    
            print(f'Contact {name.title()} does not exist.')

    def view_all(self) -> None:
        for name, details in self.contacts.items():
            print(f'- {details.title()}')


contact = AddressBook()

contact.add('David', 1234567890, 'Somewhere in Nigeria')
contact.add('DD', 9876543210, 'Another place in Nigeria')
contact.view_all()

contact.edit('David', 86420, 'Somewhere in Nigeria')
contact.view_all()

contact.delete('DD')
contact.view_all()

contact.view('DD')

contact.edit('Dee', 97531, 'A place in Nigeria')
contact.edit('DD', 13579, 'Places in Nigeria')
contact.edit('Dave', 24680, 'Any place in Nigeria')

contact.add('Dee', 97531, 'A place in Nigeria')
contact.add('DD', 13579, 'Places in Nigeria')
contact.add('Dave', 24680, 'Any place in Nigeria')

contact.view_all()