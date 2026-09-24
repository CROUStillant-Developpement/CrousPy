"""
Tests d'intégration sur les flux réels du CROUS (réseau requis).

Lancer avec : ``uv run pytest tests/test_feed_live.py``
"""

import asyncio

from aiohttp import ClientSession

from CrousPy import Crous, Menus


def menusSignature(menus: Menus) -> list:
    return [
        (
            menu.date.date().isoformat(),
            [
                (
                    meal.name,
                    [(c.name, [d.name for d in c.dishes]) for c in meal.categories],
                )
                for meal in menu.meals
            ],
        )
        for menu in menus
    ]


async def _run() -> None:
    async with ClientSession() as session:
        crous = Crous(session)

        feeds = await crous.feed.get()
        assert len(feeds) >= 26

        # Tous les flux doivent être décodables (certains contiennent des caractères de contrôle)
        byFeedId = {}
        for feed in feeds:
            rus = await crous.feed.getByURL(feed.url)
            assert len(rus) > 0, feed.name
            for ru in rus:
                byFeedId[ru.id] = ru

        # Chaque RU de l'API est présent dans les flux via RU.feedId
        regions = await crous.region.get()
        region = regions[0]
        apiRus = await crous.ru.get(region.id)
        for ru in apiRus:
            assert ru.feedId in byFeedId, ru
            assert byFeedId[ru.feedId].title == ru.title

        # Les menus du flux sont identiques à ceux de l'API
        compared = 0
        for ru in apiRus:
            feedRu = byFeedId[ru.feedId]
            if len(feedRu.menus) == 0:
                continue
            apiMenus = await crous.menu.get(region.id, ru.id)
            assert menusSignature(feedRu.menus) == menusSignature(apiMenus), ru
            compared += 1
            if compared >= 3:
                break


def test_feeds_match_api() -> None:
    asyncio.run(_run())
