from faker import Faker

fake = Faker("pl_PL")
persons = []
personsB = []


class BaseContact:
    def __init__(self, first_name, last_name, mail, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.mail = mail
        self.phone_number = phone_number

    def __str__(self):
        return f"{self.first_name} {self.last_name} " \
               f"e-mail: {self.mail} phone: {self.phone_number}"

    def contact(self):
        print(f"Kontaktuj się z: {self.first_name} {self.last_name} "
              f"e-mail: {self.mail} phone {self.phone_number}"
              )

    @property
    def label_lenght(self):
        return (len(fake.first_name() + " " + fake.last_name()))


class BusinessContact(BaseContact):
    def __init__(self, business, position, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.business = business
        self.position = position

    def __str__(self):
        return super().__str__() + f" Firma: {self.business} {self.position}"

    def contact(self):
        print(
            f"Kontaktuj się z: {self.first_name} {self.last_name} "
            f"e-mail: {self.mail} phone {self.phone_number} "
            f"stanowisko {self.business}"
        )


def FakeBaseContact(z):
    for x in range(z):
        person_ID = fake.first_name() + "_" + fake.last_name()
        person_ID = BaseContact(fake.first_name(), fake.last_name(), fake.email(), fake.phone_number())
        persons.append(person_ID)
    for person in persons:
        print(person)


def FakeBusinessContact(y):
    for x in range(y):
        person_IDB = fake.first_name() + "_" + fake.last_name()
        person_IDB = BusinessContact(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            mail=fake.company_email(),
            phone_number=fake.phone_number(),
            business=fake.company(),
            position=fake.job()
        )
        personsB.append(person_IDB)
    for personB in personsB:
        print(personB)

if __name__ == "__main__":
    what_create = input(
        "What type of contacts will be created Base/Business: "
    )
    how_many = int(input("How many contacts: "))
    if what_create == "Base":
        FakeBaseContact(how_many)
    elif what_create == "Business":
        FakeBusinessContact(how_many)
    else:
        print("Value expected: Base or Business")