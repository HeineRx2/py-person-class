class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        partner_name = person_dict.get("wife") or person_dict.get("husband")
        if partner_name:
            setattr(person, "wife", Person.people[partner_name])
            setattr(person, "husband", Person.people[partner_name])
    return list(Person.people.values())
