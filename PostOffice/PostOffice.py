class MailOffice():
    def __init__(self, mail : Mail):
        self.mail = mail

class Mail():
    def __init__(self, name , address : Address, message : Message):
        self.name = name
        self.address = address
        self.message = message
    
    def held_at(self):
        return self.address

    def contact_us(self):
        return self.message

class Address():
    def __init__(self, district, subdistrict, road, province, postalcode):
        self.district = district
        self.subDistrict = subdistrict
        self.road = road
        self.province = province
        self.postalcode = postalcode

class Message():
    def __init__(self,message=""):
        self.message = message
