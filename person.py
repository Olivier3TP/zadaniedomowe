class Address:
    def __init__(self, street, zipCode, city):
        self.street = street
        self.zipCode = zipCode
        self.city = city

class Person:
    def __init__(self, name, lastName, date, pesel, street, zipCode, city):
        self.name = name
        self.lastName = lastName
        self.date = date
        self.pesel = pesel
        self.address = Address(street, zipCode, city)

    def validate_pesel(self):
        if self.pesel.isdigit() and len(self.pesel) == 11:
            # 1-3-7-9-1-3-7-9-1-3.
            suma = ((self.pesel[0] * 1) + (self.pesel[1] * 3) + (self.pesel[2] * 7)
                    + (self.pesel[3] * 9) + (self.pesel[4] * 1) + (self.pesel[5] * 3)
                    + (self.pesel[6] * 7) + (self.pesel[7] * 9) + (self.pesel[8] * 1)
                    + (self.pesel[9] * 2))
            validate = (10 - (suma % 10))
            if validate == self.pesel[10]:
                pass
            raise ValueError("Invalid pesel")
        raise ValueError("Invalid pesel")