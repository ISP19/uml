"""Postoffice is a public department that provides a customer service to the public
   and handles their mail needs."""
class Message():
    """Message in mails"""
    def __init__(self, message=""):
        self.message = message

    def showmessage(self):
        """show message of mail"""
        return self.message

    def __str__(self):
        return self.message

class Address():
    """Address of location"""
    def __init__(self, recipientname, district, subdistrict, road, province, postalcode):
        self.recipientname = recipientname
        self.district = district
        self.subdistrict = subdistrict
        self.road = road
        self.province = province
        self.postalcode = postalcode

    def showrecipientname(self):
        """show reciever name."""
        return self.recipientname

    def showpostalcode(self):
        """show postalcode"""
        return self.postalcode

class Mail():
    """Mail class that collect sendername, address, message."""
    def __init__(self, sendername, address: Address, message: Message):
        self.sender = sendername
        self.address = address
        self.message = message
    def showsender(self):
        """show sender name who sent the mail."""
        return self.sender

    def contact(self):
        """address of destination."""
        return self.address

    def showmessage(self):
        """message in the mail."""
        return self.message


class MailOffice():
    """MailOffice that sending many mails"""
    def __init__(self, mail: Mail, deliverycost=50):
        self.mail = mail
        self.deliverycost = deliverycost

    def showdeliverycost(self):
        """show price of delivery"""
        return self.deliverycost

    def __str__(self):
        return f"{self.mail.sender} have to pay deliverycost{self.deliverycost}"
