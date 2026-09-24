import re

# Articles et particules laissés en minuscules dans un titre (sauf en première position)
_PARTICLES = {"le", "la", "les", "de", "du", "des", "d", "l", "et", "au", "aux", "en"}

# Sigles conservés en majuscules
_ACRONYMS = {
    "RU",
    "IUT",
    "INSPE",
    "ENS",
    "ENSIL",
    "ESIEE",
    "IAE",
    "IFSI",
    "FJT",
    "FEC",
    "CHU",
    "CH",
    "IEP",
    "UTT",
    "ENSAM",
}

# Sépare les mots en conservant les séparateurs (espaces, apostrophes, tirets, ...)
_SEPARATORS = re.compile(r"([\s'’&/\-()]+)")


def formatTitle(raw: str) -> str:
    """
    Formate le titre d'un restaurant.

    Les titres déjà en casse mixte (ex : « Resto U Moulin de la Housse ») sont
    conservés tels quels, seule la première lettre est mise en majuscule si besoin.
    Les titres entièrement en majuscules (ex : « RESTO U' LE CRATERE ») sont
    convertis en casse titre (« Resto U' le Cratere ») en conservant les sigles.

    :param raw: Le titre brut.
    :type raw: str

    :return: Le titre formaté.
    :rtype: str
    """
    if raw is None:
        return None

    title = re.sub(r"\s+", " ", str(raw)).strip()

    if not title:
        return title

    if title != title.upper():
        # Casse mixte : on respecte le titre d'origine
        return title[0].upper() + title[1:]

    parts = _SEPARATORS.split(title)
    first = True

    for index, part in enumerate(parts):
        if not part or _SEPARATORS.fullmatch(part):
            continue

        afterApostrophe = index > 0 and parts[index - 1][-1:] in ("'", "’")

        if part in _ACRONYMS or "." in part:
            formatted = part
        elif afterApostrophe and len(part) == 1:
            formatted = part.lower()  # « SNACK'N » -> « Snack'n »
        elif part.lower() in _PARTICLES and not first:
            formatted = part.lower()  # « L'IUT » -> « l'IUT »
        elif len(part) == 1:
            formatted = part  # Lettre isolée : « RESTO U' » -> « Resto U' »
        else:
            formatted = part[0] + part[1:].lower()

        if first:
            formatted = formatted[0].upper() + formatted[1:]
            first = False

        parts[index] = formatted

    return "".join(parts)
