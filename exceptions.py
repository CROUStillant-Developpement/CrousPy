import pytz

from datetime import datetime


class CrousAPIError(Exception):
    def __init__(self, error: str = "Une erreur est survenue lors de la requête."):
        self.error = error
        super().__init__(self.error)


class RedirectError(CrousAPIError):
    def __init__(self):
        self.error = "Redirection !"
        self.code = 302
        super().__init__(self.error)


class BadRequestError(CrousAPIError):
    def __init__(self):
        self.error = "Mauvaise requête !"
        self.code = 400
        super().__init__(self.error)


class ForbiddenError(CrousAPIError):
    def __init__(self):
        self.error = "Accès refusé !"
        self.code = 403
        super().__init__(self.error)


class RegionIntrouvable(CrousAPIError):
    def __init__(self):
        self.error = "Cette région est introuvable !"
        self.code = 404
        super().__init__(self.error)


class RestaurantIntrouvable(CrousAPIError):
    def __init__(self):
        self.error = "Ce restaurant est introuvable !"
        self.code = 404
        super().__init__(self.error)


class MenuIntrouvable(CrousAPIError):
    def __init__(self):
        self.error = "Le menu n'est pas disponible !"
        self.code = 404
        self.date = datetime.now(tz=pytz.timezone("Europe/Paris"))
        super().__init__(self.error)


class ConflictWithServer(CrousAPIError):
    def __init__(self):
        self.error = "Conflit avec le serveur !"
        self.code = 409
        super().__init__(self.error)


class TeapotError(CrousAPIError):
    def __init__(self):
        self.error = "Je suis une théière !"
        self.code = 418
        super().__init__(self.error)


class TooEarlyError(CrousAPIError):
    def __init__(self):
        self.error = "Trop tôt !"
        self.code = 425
        super().__init__(self.error)


class InternalServerError(CrousAPIError):
    def __init__(self):
        self.error = "Erreur interne du serveur !"
        self.code = 500
        super().__init__(self.error)
