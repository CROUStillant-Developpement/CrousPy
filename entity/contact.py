import html


class Contact:
    """
    Représente les informations de contact d'un RU.
    
    :param data: Les données de contact.
    :type data: str
    
    :ivar data: Les données de contact.
    :vartype data: str

    :ivar name: Le nom.
    :vartype name: str

    :ivar address: L'adresse.
    :vartype address: str

    :ivar phone: Le numéro de téléphone.
    :vartype phone: str

    :ivar email: L'adresse email.
    :vartype email: str
    """
    def __init__(self, data: str) -> None:
        self.__data = data

        self.__name = html.unescape(self.__data.split("<h2>")[1].split("</h2>")[0]).lstrip()
        self.__address = self.__data.split("<p>")[1].split("<br/>")[0].replace("</p>", "")

        try:
            self.__phone = self.__data.split("<b>T&#233;l&#233;phone</b> : ")[1].split("<br/>")[0].replace(" ", ".").replace("</p>", "")
            if "pas.de.telephone" in self.__phone.lower():
                raise Exception("Pas de téléphone")
            
            if self.__phone.startswith("."):
                self.__phone = self.__phone[1:]

            if self.__phone.endswith(".o"):
                self.__phone = self.__phone[:-2]

            if "/" in self.__phone:
                self.__phone = self.__phone.split("/")[0]
                self.__phone.strip()

            if len(self.__phone) == 10:
                self.__phone = f"{self.__phone[0:2]}.{self.__phone[2:4]}.{self.__phone[4:6]}.{self.__phone[6:8]}.{self.__phone[8:10]}"

            if len(self.__phone) > 14:
                self.__phone = self.__phone[0:14]
        except:
            self.__phone = None

        try:
            self.__email = self.__data.split("<b>E-mail</b> : ")[1].split("</p>")[0]
        except:
            self.__email = None


    @property
    def data(self) -> str:
        return self.__data
    
    @property
    def name(self) -> str:
        return self.__name
    
    @property
    def address(self) -> str:
        return self.__address
    
    @property
    def phone(self) -> str:
        return self.__phone
    
    @property
    def email(self) -> str:
        return self.__email
    

    def __repr__(self) -> str:
        return f"<Contact name={self.name} address={self.address} phone={self.phone} email={self.email}>"
