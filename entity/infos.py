import re

from typing import TypedDict


class InfosData(TypedDict):
    """
    Représente les données d'un RU.
    
    :param data: Les données du RU.
    :type data: str

    :param horaires: Les horaires.
    :type horaires: list

    :param pmr: Si le RU est accessible aux personnes à mobilité réduite.
    :type pmr: bool

    :param acces: Les moyens d'accès.
    :type acces: list

    :param pratique: Les informations pratiques.
    :type pratique: str

    :param paiements: Les moyens de paiement.
    :type paiements: list
    """
    data: str
    horaires: list
    pmr: bool
    acces: list
    pratique: str
    paiements: list


class Infos:
    """
    Représente les informations d'un RU.
    
    :param data: Les données du RU.
    :type data: str

    :ivar data: Les données du RU.
    :vartype data: str

    :ivar horaires: Les horaires.
    :vartype horaires: list

    :ivar pmr: Si le RU est accessible aux personnes à mobilité réduite.
    :vartype pmr: bool

    :ivar acces: Les moyens d'accès.
    :vartype acces: list

    :ivar pratique: Les informations pratiques.
    :vartype pratique: str

    :ivar paiements: Les moyens de paiement.
    :vartype paiements: list
    """
    def __init__(self, data: InfosData) -> None:
        self.__data: dict = data

        if data == '  <img src=\"\" class=\"image-batiment\"> ':
            self.__horaires = ["", []]
            self.__pmr = None
            self.__acces = None
            self.__pratique = None
            self.__paiements = []
            return

        if "Horaires" in data:
            self.__horaires: list = data.split("<h2>Horaires</h2>")[1]
        else:
            self.__horaires = ""

        if "Moyen d'accès" in self.__horaires:
            self.__horaires = self.__horaires.split("<h2>Moyen d'accès</h2>")[0].replace("<p>", "").replace("</p>", "").strip().split("<br/>")
        elif "Paiements possibles" in self.__horaires:
            self.__horaires = self.__horaires.split("<h2>Paiements possibles</h2>")[0].replace("<p>", "").replace("</p>", "").strip().split("<br/>")
        else:
            self.__horaires = [self.__horaires.replace("<p>", "").replace("</p>", "").strip()]

        self.__horaires.append([])

        if "Pratique" in self.__horaires[0]:
            self.__horaires = [self.__horaires[0].split("<h2>Pratique</h2>")[0], []]

        if "Pratique" in self.__horaires[1]:
            self.__horaires[1] = self.__horaires[1].split("<h2>Pratique</h2>")[0].strip()

        if self.__horaires[0].startswith("- "):
            self.__horaires[0] = self.__horaires[0][2:]

        if self.__horaires[0].endswith(":"):
            self.__horaires[0] = self.__horaires[0][:-1]

        if self.__horaires[1] == "":
            self.__horaires = [self.__horaires[0], []]


        matches = re.finditer(r"\d{4,}", self.__horaires[0])

        for matchNum, match in enumerate(matches, start=1):
            self.__horaires[0] = self.__horaires[0].replace(match.group(), f"{match.group()[0:2]}h{match.group()[2:4]}")

        if isinstance(self.__horaires[1], str) and self.__horaires[1].startswith("- "):
            self.__horaires[1] = self.__horaires[1][2:]

        newHoraires = []
        for h in self.__horaires:
            if "<h2>Pratique</h2>" in h:
                newHoraires.append(h.split("<h2>Pratique</h2>")[0])
            else:
                newHoraires.append(h)
        self.__horaires = newHoraires

        if [] in self.__horaires:
            self.__horaires.remove([])

        if "" in self.__horaires:
            self.__horaires.remove("")

        for i in range(len(self.__horaires)):
            self.__horaires[i] = self.__horaires[i].strip()

        self.__pmr = True if "Accessible aux personnes à mobilité réduite" in data else False

        try:
            self.__acces = data.split("<h2>Moyen d'accès</h2>")[1]
            
            if "Pratique" in self.__acces:
                self.__acces = self.__acces.split("<h2>Pratique</h2>")[0].replace("<p>", "").replace("</p>", "").strip().replace("BUS ligne", "Bus :").replace(" et ", ", ").split("<br/>")
            elif "Paiements possibles" in self.__acces:
                self.__acces = self.__acces.split("<h2>Paiements possibles</h2>")[0].replace("<p>", "").replace("</p>", "").strip().replace("BUS ligne", "Bus :").replace(" et ", ", ").split("<br/>")
        except:
            self.__acces = None

        if self.__acces:
            if "" in self.__acces:
                self.__acces.remove("")

            if self.__acces[0] == "---":
                self.__acces = None

        try:
            self.__pratique = data.split("<h2>Pratique</h2>")[1].split("<h2>Paiements possibles</h2>")[0]
        except:
            self.__pratique = None

        try:
            self.__paiements = data.split("<h2>Paiements possibles</h2>")[1].replace("especes", "Espèces").split("</p>")[0].split("<br/>")[0:2]
        except:
            self.__paiements = []
    
        try:
            self.__paiements[0] = self.__paiements[0].split("'/>")[1].split("<br/>")[0].strip()
        except:
            pass

        try:
            self.__paiements[1] = self.__paiements[1].split("'/>")[1].split("<br/>")[0].strip()
        except:
            pass

        if self.__paiements and (self.__paiements[1] == "" or self.__paiements[1] == " "):
            self.__paiements = [self.__paiements[0]]
            
        if [] in self.__paiements:
            self.__paiements.remove([])


    @property
    def data(self) -> str:
        return self.__data

    @property
    def horaires(self) -> list:
        return self.__horaires

    @property
    def pmr(self) -> bool:
        return self.__pmr

    @property
    def acces(self) -> list:
        return self.__acces

    @property
    def pratique(self) -> str:
        return self.__pratique

    @property
    def paiements(self) -> list:
        return self.__paiements


    def __repr__(self) -> str:
        return f"<Infos horaires={self.horaires} pmr={self.pmr} acces={self.acces} pratique={self.pratique} paiements={self.paiements}>"
