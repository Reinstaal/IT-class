# Übung Wiedereinstieg OOP
# Schritt 1: Die Basis-Klasse Kontakt
# Erstellen Sie eine Klasse namens Kontakt.
# Attribute (Instanzvariablen):
# name (String, Required)
# telefonnummer (String, Required)
# email (String, Optional)
# Methoden:
# __init__(self, name, telefonnummer, email=None): Der Konstruktor zur Initialisierung der Attribute.
# __str__(self): Eine magische Methode, die eine lesbare String-Repräsentation des Kontakts zurückgibt (z.B. "Name: Max Mustermann, Tel: 12345, E-Mail: max@mail.de").
# __repr__(self): Eine magische Methode, die die offizielle String-Repräsentation zurückgibt, die das Objekt eindeutig beschreibt (hilfreich beim Debugging).
# Schritt 2: Die Manager-Klasse Telefonbuch
# Erstellen Sie eine Klasse namens Telefonbuch, die alle Kontakt-Objekte verwaltet.
# Attribut:
# kontakte: Eine Liste, in der alle Kontakt-Objekte gespeichert werden sollen (z.B. self._kontakte = []).
# Methoden:
# kontakt_hinzufuegen(self, kontakt): Fügt ein Kontakt-Objekt zur internen Liste hinzu.
# kontakt_suchen(self, suchbegriff): Sucht nach Kontakten. Implementieren Sie eine einfache Suche, die alle Kontakt-Objekte zurückgibt, deren Name den suchbegriff enthält (Groß-/Kleinschreibung ignorieren).
 
class Contact():
    def __init__(self, name, phoneNumber, email=None):
        self.name = name
        self.phoneNumber = phoneNumber
        if email:
            self.email = email
        else:
            self.email = "No mail saved"

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phoneNumber}, E-Mail: {self.email}"
    
    def __repr__(self):
        return (f"Contact(name='{self.name}', "
                f"phoneNumber='{self.phoneNumber}', "
                f"email='{self.email}')")

class PhoneBook():
    def __init__(self): 
        self._contacts = []

    def addContact(self, contact):
        self._contacts.append(contact)
        return
    
    def showContacts(self):
        contactList = []
        for i in self._contacts:
            contactList.append((i.name))
        return contactList
    
    def searchContacts(self, query):
        query = query.lower()
        hits = []

        for contact in self._contacts:
            name_lower = contact.name.lower()
            if query in name_lower:
                hits.append(contact)
        return hits


moxie = Contact("Moxie Musterfrau", 45678, "Moxie_M@mail.de")
max = Contact("Max Mustermann", 12345)

print(moxie.__str__())
print(max.__str__())


PBJames = PhoneBook()
PBJames.addContact(moxie)
PBJames.addContact(max)

print(PBJames.showContacts())
print(PBJames.searchContacts("M"))