class MailOffice():
    def __init__(self, mail : Mail):
        self.mail = mail

class Mail():
    def __init__(self, sendername , address : Address, message : Message):
        self.sender = sendername
        self.address = address
        self.message = message
    
    def sender(self):
        return self.sender

    def contact(self):
        return self.address

    def message(self):
        return self.message

class Address():
    def __init__(self,recipientname, district, subdistrict, road, province, postalcode):
        self.recipientname = recipientname
        self.district = district
        self.subdistrict = subdistrict
        self.road = road
        self.province = province
        self.postalcode = postalcode

class Message():
    def __init__(self,message=""):
        self.message = message
