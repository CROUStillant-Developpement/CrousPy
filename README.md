<div align="center">
<img src="https://croustillant.menu/logo.png" alt="CROUStillant Logo"/>
  
# CROUStillant
CROUStillant est un projet qui a pour but de fournir les menus des restaurants universitaires en France et en Outre-Mer. 

</div>
  
# 📖 • Sommaire

- [🚀 • Présentation](#--présentation)
- [📦 • Installation](#--installation)
- [💻 • Développement](#--développement)
- [📄 • Utilisation](#--utilisation)
- [⚠️ • Exceptions](#️--exceptions)
- [📃 • Crédits](#--crédits)
- [📝 • License](#--license)

# 🚀 • Présentation

Ce dépôt contient le code source d'une librairie interne de CROUStillant en Python qui permet d'interagir avec l'API du CROUS. Si vous souhaitez récupérer les menus des restaurants universitaires en France et en Outre-Mer, utilisez notre API publique [api.croustillant.menu](https://api.croustillant.menu).

# 📦 • Installation

```bash
pip install git+https://github.com/CROUStillant-Developpement/CrousPy
```

Ou avec [uv](https://github.com/astral-sh/uv) :

```bash
uv add git+https://github.com/CROUStillant-Developpement/CrousPy
```

# 💻 • Développement

Pour installer la librairie en mode de développement, exécutez les commandes suivantes :

1. Cloner le dépôt
```bash
git clone https://github.com/CROUStillant-Developpement/CrousPy
```

2. Se placer dans le répertoire du projet
```bash
cd CrousPy
```

3. Créer un environnement virtuel et installer les dépendances
```bash
uv sync
```

# 📄 • Utilisation

```python
import asyncio

from CrousPy import Crous
from aiohttp import ClientSession


async def main():
    session = ClientSession()

    client = Crous(session=session)

    # Récupérer toutes les régions
    regions = await client.region.get()
    print(regions)

    # Récupérer une région par son ID
    region = await client.region.getById(regionID=23)
    print(region)

    # Récupérer les restaurants d'une région
    restaurants = await client.ru.get(regionID=23)
    print(restaurants)

    # Récupérer un restaurant par son ID
    restaurant = await client.ru.getById(regionID=23, rid=1)
    print(restaurant)

    # Récupérer les menus d'un restaurant
    menus = await client.menu.get(regionID=23, rid=1)
    print(menus)

    # Récupérer le menu d'un restaurant par sa date (format : YYYY-MM-DD)
    menu = await client.menu.getByDate(regionID=23, rid=1, date="2026-04-28")
    print(menu)

    await session.close()


if __name__ == "__main__":
    asyncio.run(main())
```

# ⚠️ • Exceptions

| Exception | Code HTTP | Description |
|---|---|---|
| `CrousAPIError` | - | Erreur générique de l'API |
| `RedirectError` | 302 | Redirection inattendue |
| `BadRequestError` | 400 | Mauvaise requête |
| `ForbiddenError` | 403 | Accès refusé |
| `RegionIntrouvable` | 404 | Région introuvable |
| `RestaurantIntrouvable` | 404 | Restaurant introuvable |
| `MenuIntrouvable` | 404 | Menu introuvable |
| `ConflictWithServer` | 409 | Conflit avec le serveur |
| `TeapotError` | 418 | Je suis une théière |
| `TooEarlyError` | 425 | Requête trop précoce |
| `InternalServerError` | 500 | Erreur interne du serveur |

# 📃 • Crédits

- [CROUStillant Développement](https://croustillant.menu/fr/about#team) - L'équipe de CROUStillant Développement

# 📝 • License

CROUStillant sous licence [Apache 2.0](LICENSE).

```
Copyright 2024 CROUStillant Développement

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
