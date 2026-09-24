import pytest

from CrousPy import formatTitle


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        # Casse mixte : conservée telle quelle
        ("Resto U Moulin de la Housse", "Resto U Moulin de la Housse"),
        ("Resto U' la Vague", "Resto U' la Vague"),
        ("Cafétéria l'EsCaLe ", "Cafétéria l'EsCaLe"),
        ("R.U. Le Rambouillet  (Cambrai)", "R.U. Le Rambouillet (Cambrai)"),
        # Casse mixte commençant par une minuscule : seule la première lettre change
        ("cafétéria la Terrasse", "Cafétéria la Terrasse"),
        # Tout en majuscules : casse titre, sigles conservés
        ("RESTO U'  LE CRATERE", "Resto U' le Cratere"),
        ("RU ENSIL", "RU ENSIL"),
        ("CROUS & GO' LE SAXO", "Crous & Go' le Saxo"),
        ("IFSI MAUBERT", "IFSI Maubert"),
        ("SNACK'N SWING", "Snack'n Swing"),
        ("RESTO U' DE L'IUT", "Resto U' de l'IUT"),
        ("RESTO U' CLOS SAINT-JACQUES / DOLET", "Resto U' Clos Saint-Jacques / Dolet"),
        ("LE PHARE ", "Le Phare"),
        ("F.J.T RABELAIS", "F.J.T Rabelais"),
        ("FEC", "FEC"),
        ("MINI R", "Mini R"),
    ],
)
def test_format_title(raw: str, expected: str) -> None:
    assert formatTitle(raw) == expected


def test_format_title_empty() -> None:
    assert formatTitle(None) is None
    assert formatTitle("   ") == ""
