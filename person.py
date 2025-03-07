from datetime import datetime


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
                    + (self.pesel[9] * 3))
            validate = (10 - (suma % 10) % 10)
            if validate == self.pesel[10]:
                year = self.pesel[0:2]
                month = self.pesel[2:4]
                day = self.pesel[4:6]

                if 81 <= month <= 92:
                    year += 1800
                elif 1 <= month <= 12:
                    year += 1900
                elif 21 <= month <= 32:
                    year += 2000
                    month -= 20
                elif 41 <= month <= 52:
                    year += 2100
                    month -= 40
                elif 61 <= month <= 72:
                    year += 2200
                    month -= 60

                birth_date = datetime(day, month, year)

                if birth_date == self.date:
                    pass

        raise ValueError("Invalid pesel")
