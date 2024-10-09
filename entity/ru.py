from .infos import Infos
from .contact import Contact
from typing import TypedDict


class RUData(TypedDict):
    """
    Définit la structure des données d'un RU.
    
    :param album_url: L'URL de l'album.
    :type album_url: str
    
    :param closing: Si le RU est fermé.
    :type closing: str
    
    :param contact: Les informations de contact.
    :type contact: dict
    
    :param crous_and_go_url: L'URL Crous&Go.
    :type crous_and_go_url: str
    
    :param id: L'ID du RU.
    :type id: int
    
    :param image_url: L'URL de l'image.
    :type image_url: str
    
    :param infos: Les informations.
    :type infos: dict
    
    :param lastUpdate: La dernière mise à jour.
    :type lastUpdate: str
    
    :param lat: La latitude.
    :type lat: float
    
    :param lon: La longitude.
    :type lon: float
    
    :param opening: L'heure d'ouverture.
    :type opening: str
    
    :param originalImageUrl: L'URL de l'image originale.
    :type originalImageUrl: str
    
    :param regionId: L'ID de la région.
    :type regionId: int

    :param sharing_short_url: L'URL de partage courte.
    :type sharing_short_url: str

    :param sharing_url: L'URL de partage.
    :type sharing_url: str

    :param short_desc: La description courte.
    :type short_desc: str

    :param synchronized1: Si le RU est synchronisé.
    :type synchronized1: bool

    :param thumbnail_url: L'URL de la miniature.
    :type thumbnail_url: str

    :param title: Le titre.
    :type title: str

    :param type: Le type.
    :type type: str

    :param virtual_visit_url: L'URL de la visite virtuelle.
    :type virtual_visit_url: str

    :param xmlid: L'ID XML.
    :type xmlid: str

    :param zone: La zone.
    :type zone: str
    """
    album_url: str
    closing: str
    contact: Contact
    crous_and_go_url: str
    id: int
    image_url: str
    infos: Infos
    lastUpdate: str
    lat: float
    lon: float
    opening: str
    originalImageUrl: str
    regionId: int
    sharing_short_url: str
    sharing_url: str
    short_desc: str
    synchronized1: bool
    thumbnail_url: str
    title: str
    type: str
    virtual_visit_url: str
    xmlid: str
    zone: str


class RU:
    """
    Représente un Restaurant Universitaire.
    
    :param data: Les données du RU.
    :type data: dict
    
    :ivar data: Les données du RU.
    :vartype data: dict
    
    :ivar album_url: L'URL de l'album.
    :vartype album_url: str
    
    :ivar open: Si le RU est ouvert.
    :vartype open: bool
    
    :ivar contact: Les informations de contact.
    :vartype contact: Contact
    
    :ivar crous_and_go_url: L'URL Crous&Go.
    :vartype crous_and_go_url: str
    
    :ivar id: L'ID du RU.
    :vartype id: int
    
    :ivar image_url: L'URL de l'image.
    :vartype image_url: str
    
    :ivar infos: Les informations.
    :vartype infos: Infos
    
    :ivar lastUpdate: La dernière mise à jour.
    :vartype lastUpdate: str
    
    :ivar lat: La latitude.
    :vartype lat: float
    
    :ivar lon: La longitude.
    :vartype lon: float
    
    :ivar opening: L'heure d'ouverture.
    :vartype opening: str
    
    :ivar originalImageUrl: L'URL de l'image originale.
    :vartype originalImageUrl: str
    
    :ivar regionId: L'ID de la région.
    :vartype regionId: int
    
    :ivar sharing_short_url: L'URL de partage courte.
    :vartype sharing_short_url: str
    
    :ivar sharing_url: L'URL de partage.
    :vartype sharing_url: str
    
    :ivar short_desc: La description courte.
    :vartype short_desc: str
    
    :ivar synchronized1: Si le RU est synchronisé.
    :vartype synchronized1: bool
    
    :ivar thumbnail_url: L'URL de la miniature.
    :vartype thumbnail_url: str
    
    :ivar title: Le titre.
    :vartype title: str
    
    :ivar type: Le type.
    :vartype type: str
    
    :ivar virtual_visit_url: L'URL de la visite virtuelle.
    :vartype virtual_visit_url: str
    
    :ivar xmlid: L'ID XML.
    :vartype xmlid: str
    
    :ivar zone: La zone.
    :vartype zone: str
    """
    def __init__(self, data: RUData) -> None:
        self.__data: dict = data


        self.__image_url = self.__data.get("image_url")
        if self.__image_url == "https://admin-v2.crous-mobile.fr/media/":
            self.__image_url = None
        else:
            self.__image_url = self.__image_url.replace("//", "")


    @property
    def data(self) -> dict:
        return self.__data
    
    @property
    def album_url(self) -> str:
        return self.__data.get("album_url")
    
    @property
    def open(self) -> bool:
        return True if self.__data.get("closing") == "0" else False
    
    @property
    def contact(self) -> Contact:
        return Contact(self.__data.get("contact"))
    
    @property
    def crous_and_go_url(self) -> str:
        return self.__data.get("crous_and_go_url")
    
    @property
    def id(self) -> int:
        return self.__data.get("id")
    
    @property
    def image_url(self) -> str:
        return self.__image_url
    
    @property
    def infos(self) -> Infos:
        return Infos(self.__data.get("infos"))
    
    @property
    def lastUpdate(self) -> str:
        return self.__data.get("lastUpdate")
    
    @property
    def lat(self) -> float:
        return self.__data.get("lat")
    
    @property
    def lon(self) -> float:
        return self.__data.get("lon")
    
    @property
    def opening(self) -> str:
        return self.__data.get("opening")
    
    @property
    def originalImageUrl(self) -> str:
        return self.__data.get("originalImageUrl")
    
    @property
    def regionId(self) -> int:
        return self.__data.get("regionId")
    
    @property
    def sharing_short_url(self) -> str:
        return self.__data.get("sharing_short_url")
    
    @property
    def sharing_url(self) -> str:
        return self.__data.get("sharing_url")
    
    @property
    def short_desc(self) -> str:
        return self.__data.get("short_desc")
    
    @property
    def synchronized1(self) -> bool:
        return self.__data.get("synchronized1")
    
    @property
    def thumbnail_url(self) -> str:
        return self.__data.get("thumbnail_url")
    
    @property
    def title(self) -> str:
        return self.__data.get("title")
    
    @property
    def type(self) -> str:
        return self.__data.get("type")
    
    @property
    def virtual_visit_url(self) -> str:
        return self.__data.get("virtual_visit_url")
    
    @property
    def xmlid(self) -> str:
        return self.__data.get("xmlid")
    
    @property
    def zone(self) -> str:
        return self.__data.get("zone").lower().capitalize()


    def __repr__(self) -> str:
        return f"<RU title={self.title} id={self.id} zone={self.zone}>"
