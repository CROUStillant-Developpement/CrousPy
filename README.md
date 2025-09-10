<div align="center">
<img src="https://croustillant.menu/logo.png" alt="CROUStillant Logo"/>
  
# CROUStillant
CROUStillant est un projet qui a pour but de fournir les menus des restaurants universitaires en France et en Outre-Mer. 

</div>
  
# 📖 • Sommaire

- [🚀 • Présentation](#--présentation)
- [⚙️ • Installation](#--installation)
- [💻 • Développement](#--développement)
- [📄 • Utilisation](#--utilisation)
- [📃 • Crédits](#--crédits)
- [📝 • License](#--license)

# 🚀 • Présentation

Ce dépôt contient le code source d'une librairie interne de CROUStillant en Python qui permet d’interagir avec l'API du CROUS. Si vous souhaitez récupérer les menus des restaurants universitaires en France et en Outre-Mer, utilisez notre API publique [api.croustillant.menu](https://api.croustillant.menu).

# 💻 • Développement

Pour installer la librairie en mode de développement, exécutez les commandes suivantes :

1. Cloner le dépôt
```bash
git clone https://github.com/CROUStillant-Developpement/CrousPy
```

2. Créer un environnement virtuel et installer les dépendances
```bash
cd CrousPy
```

3. Créer un environnement virtuel
```bash	
uv sync
```

# 📄 • Utilisation

```python
import asyncio

from CrousPy import Crous
from aiohttp import ClientSession


async def main():
    """
    Exemple d'utilisation de la librairie CrousPy
    """
    session = ClientSession()

    client = Crous(session=session)

    # Récupérer les régions
    regions = await client.region.get()

    print(regions)

    # Récupérer les restaurants
    restaurants = await client.ru.get(regionID=23)

    print(restaurants)

    # Récupérer les menus
    menus = await client.menu.get(regionID=23, ruID=1)

    print(menus)

    await session.close()


if __name__ == "__main__":
    asyncio.run(main())
```

# 📃 • Crédits

- [Paul Bayfield](https://github.com/PaulBayfield) - Fondateur du projet et développeur principal

# 📝 • License

CROUStillant sous licence [Apache 2.0](LICENSE).

```
Copyright 2024 - 2025 CROUStillant Développement

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
